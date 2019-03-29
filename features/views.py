from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Feature, TicketComment
from .forms import TicketForm, CommentForm



@login_required()
def get_features(request):
    """
    Create a view that will return a
    list of tickets that were published prior to'now'
    and render them to the 'tickets.html' template
    """
    features = Feature.objects.filter(most_recent_update__lte=timezone.now()
                                ).order_by('-most_recent_update')
    return render(request, "get_features.html", {'features': features})
    
    
@login_required() 
def feature_view(request, pk):
    """
    Create a view that will return a single ticket
    object based on the ticket ID and render it
    to the 'ticket_view.html' template, return a
    comment form for users to add a comment,
    and return all previously added comments,
    or return a 404 error if ticket is not found
    """
    feature = get_object_or_404(Feature, pk=pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST, request.FILES)
        
        if comment_form.is_valid():
            ticketComment = comment_form.save(commit=False)
            ticketComment.ticket = feature
            ticketComment.user = request.user
            ticketComment.save()
            return redirect(reverse('feature_view', kwargs={'pk': pk}))
            
    else:
        comment_form = CommentForm()
        feature_comments = TicketComment.objects.filter(ticket__pk=feature.pk)
        feature.views += 1
        feature.save()
        return render(request, 'feature_view.html', {'feature':feature, 'feature_comments':feature_comments, 'comment_form':comment_form})

def create_or_edit_feature(request, pk=None):
    """
     Create a view that allows a user to create
     or edit a ticket depending on if the
     ticket ID is null or not
     """
    feature = get_object_or_404(Feature, pk=pk) if pk else None
    if request.method == "POST":
        feature_form = TicketForm(request.POST, request.FILES, instance=feature)
        if feature_form.is_valid():
            feature = feature_form.save()
            feature.author = request.user
            feature.save()
            return redirect(feature_view, feature.pk)
    else:
        feature_form = TicketForm(instance=feature)
    return render(request, 'feature_form.html', {'feature_form': feature_form})        


@login_required() 
def delete_feature(request, pk):
    """
    Delete a bug
    """
    feature =  get_object_or_404(Feature, pk=pk) 
    feature.delete()
    return redirect('profile')
     
        
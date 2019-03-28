from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Bug, TicketComment
from .forms import TicketForm, CommentForm



@login_required()
def get_bugs(request):
    """
    Create a view that will return a
    list of tickets that were published prior to'now'
    and render them to the 'tickets.html' template
    """
    bugs = Bug.objects.filter(most_recent_update__lte=timezone.now()
                                ).order_by('-most_recent_update')
    return render(request, "get_bugs.html", {'bugs': bugs})
    
    
@login_required() 
def bug_view(request, pk):
    """
    Create a view that will return a single ticket
    object based on the ticket ID and render it
    to the 'ticket_view.html' template, return a
    comment form for users to add a comment,
    and return all previously added comments,
    or return a 404 error if ticket is not found
    """
    bug = get_object_or_404(Bug, pk=pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST, request.FILES)
        
        if comment_form.is_valid():
            ticketComment = comment_form.save(commit=False)
            ticketComment.ticket = bug
            ticketComment.user = request.user
            ticketComment.save()
            return redirect(reverse('bug_view', kwargs={'pk': pk}))
            
    else:
        comment_form = CommentForm()
        bug_comments = TicketComment.objects.filter(ticket__pk=bug.pk)
        bug.views += 1
        bug.save()
        return render(request, 'bug_view.html', {'bug':bug, 'bug_comments':bug_comments, 'comment_form':comment_form})

def create_or_edit_bug(request, pk=None):
    """
     Create a view that allows a user to create
     or edit a ticket depending on if the
     ticket ID is null or not
     """
    bug = get_object_or_404(Bug, pk=pk) if pk else None
    if request.method == "POST":
        bug_form = TicketForm(request.POST, request.FILES, instance=bug)
        if bug_form.is_valid():
            bug = bug_form.save()
            bug.author = request.user
            bug.save()
            return redirect(bug_view, bug.pk)
    else:
        bug_form = TicketForm(instance=bug)
    return render(request, 'bug_form.html', {'bug_form': bug_form})        


@login_required() 
def delete_bug(request, pk):
     bug =  get_object_or_404(Bug, pk=pk) 
     bug.delete()
     return redirect('profile')
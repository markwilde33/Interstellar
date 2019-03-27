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
from django import forms
from .models import Feature, TicketComment

# The form for a ticket
class TicketForm(forms.ModelForm):
    
    class Meta:
        model = Feature
        fields = ('title', 'description')

# The form for a comment
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = TicketComment
        fields = ( 'comment', )
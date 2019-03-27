from django.contrib import admin
from .models import Bug, TicketComment

admin.site.register(Bug)
admin.site.register(TicketComment)
from django.contrib import admin

from apps.ticket.models import Comment, Ticket

admin.site.register(Ticket)
admin.site.register(Comment)

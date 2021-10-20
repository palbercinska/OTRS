from apps.ticket.models import Ticket, Comment
from django.forms import ModelForm, CharField, Textarea
from django import forms
import datetime


class TicketForm(ModelForm):

    CATEGORY = (

        ('SOFTWARE', 'SOFTWARE'),
        ('HARDWARE', 'HARDWARE'),
    )

    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ['customer', 'engineer', 'ticket_status']

    ticket_type = forms.CharField(label='Rodzaj zgłoszenia',
                                  widget=forms.RadioSelect(choices=CATEGORY))


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['user', 'create_time', 'ticket']

    text = forms.CharField(widget=forms.Textarea)


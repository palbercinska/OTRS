from apps.ticket.models import Ticket, Comment
from django.forms import ModelForm, CharField, Textarea
from django import forms
import datetime


class TicketForm(ModelForm):
    STATUS = (

        ('CLOSE_POSITIVE', 'CLOSE_POSITIVE'),
        ('CLOSE_NEGATIVE', 'CLOSE_NEGATIVE'),
    )
    ticket_status = forms.CharField(label='Status',
                                    widget=forms.RadioSelect(choices=STATUS))

    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ['customer', 'engineer', 'ticket_type', 'descriptions']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['user', 'create_time', 'ticket']

    text = forms.CharField(widget=forms.Textarea)

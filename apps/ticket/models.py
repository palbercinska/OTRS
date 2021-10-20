from django.forms import models
from django.db import models
from django.urls import reverse
from apps.user.models import CustomUser


class Ticket(models.Model):
    STATUS = (

        ('OPEN', 'OPEN'),
        ('PENDING', 'PENDING'),
        ('CLOSE_POSITIVE', 'CLOSE_POSITIVE'),
        ('CLOSE_NEGATIVE', 'CLOSE_NEGATIVE'),

    )

    CATEGORY = (

        ('SOFTWARE', 'SOFTWARE'),
        ('HARDWARE', 'HARDWARE'),

    )
    create_time = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(CustomUser, related_name='customer', on_delete=models.CASCADE)
    engineer = models.ForeignKey(CustomUser, related_name='engineer', on_delete=models.CASCADE, blank=True, null=True)
    ticket_status = models.CharField(max_length=20, choices=STATUS, default='PENDING')
    ticket_type = models.CharField(max_length=100, choices=CATEGORY)
    descriptions = models.TextField()

    class Meta:
        ordering = ['-create_time']

    def __str__(self):
        return '{0}'.format(self.create_time)


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_time']

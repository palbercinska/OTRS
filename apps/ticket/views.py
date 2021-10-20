from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from apps.ticket.forms import TicketForm, CommentForm
from apps.ticket.models import Ticket, Comment


class TicketView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'ticket/tickets.html'
    paginate_by = 3
    login_url = reverse_lazy('user:login')

    def get_queryset(self):
        query = Ticket.objects.filter(customer=self.request.user)
        return query.all()


class TicketCreateView(LoginRequiredMixin, CreateView):
    template_name = 'ticket/create_ticket.html'
    form_class = TicketForm
    login_url = reverse_lazy('user:login')
    success_url = reverse_lazy('ticket_list')

    def form_valid(self, form):
        form.instance.customer = self.request.user
        form.instance.ticket_status = 'PENDING'
        return super().form_valid(form)


class TicketUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'ticket/create_ticket.html'
    model = Ticket
    form_class = TicketForm
    login_url = reverse_lazy('user:login')
    success_url = reverse_lazy('ticket_list')


class TicketDeleteView(DeleteView, LoginRequiredMixin):
    template_name = 'ticket/tickets_delete.html'
    model = Ticket
    login_url = reverse_lazy('user:login')
    success_url = reverse_lazy('ticket_list')


class TicketDetailView(DetailView, LoginRequiredMixin):
    template_name = 'ticket/ticket_detail.html'
    model = Ticket
    login_url = reverse_lazy('user:login')


class CommentView(ListView, LoginRequiredMixin):
    model = Comment
    template_name = 'comment/comment.html'
    login_url = reverse_lazy('user:login')

    def get_context_data(self, **kwargs):
        context = super(CommentView, self).get_context_data(**kwargs)
        context['comment_list'] = Comment.objects.filter(ticket__id=self.kwargs['pk'])
        context['ticket_id'] = self.kwargs['pk']
        return context


class CommentCreateView(CreateView, LoginRequiredMixin):
    template_name = 'comment/comment_create.html'
    form_class = CommentForm
    login_url = reverse_lazy('user:login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.ticket = Ticket.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('comment_list', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticket_id'] = self.kwargs['pk']
        return context


class CommentDeleteView(DeleteView, LoginRequiredMixin):
    template_name = 'comment/comment_delete.html'
    model = Comment
    login_url = reverse_lazy('user:login')

    def get_success_url(self):
        return reverse_lazy('comment_list', kwargs={'pk': self.kwargs['pk']})

    def get_object(self, queryset=None):
        return Comment.objects.get(id=self.kwargs['comment_pk'])
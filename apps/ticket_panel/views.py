from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from apps.ticket.models import Ticket, Comment
from apps.ticket_panel.forms import CommentForm, TicketForm


class StatusView(View):
    model = None
    ticket_status_type = None

    def post(self, request, pk):
        ticket = Ticket.objects.filter(pk=pk).first()
        if ticket.engineer is None:
            ticket.engineer = request.user
            ticket.ticket_status = 'OPEN'
        else:
            ticket.engineer = None
            ticket.ticket_status = 'PENDING'
        ticket.save()
        return redirect(reverse('ticket_panel_list'))


class TicketView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'ticket_panel/ticket_panel_list.html'
    paginate_by = 3
    login_url = reverse_lazy('user:login')


class TicketDetailView(DetailView, LoginRequiredMixin):
    template_name = 'ticket_panel/ticket_panel_detail.html'
    model = Ticket
    login_url = reverse_lazy('user:login')


class TicketUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'ticket_panel/ticket_panel_create_ticket.html'
    model = Ticket
    form_class = TicketForm
    login_url = reverse_lazy('user:login')
    success_url = reverse_lazy('ticket_panel_list')


# class CommentView(ListView, LoginRequiredMixin):
#     model = Comment
#     template_name = 'comment/comment.html'
#     login_url = reverse_lazy('user:login')
#
#
# class CommentCreateView(CreateView, LoginRequiredMixin):
#     template_name = 'comment/comment_create.html'
#     form_class = CommentForm
#     success_url = reverse_lazy('comment_list')
#     login_url = reverse_lazy('user:login')
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         ticket_pk = self.kwargs.get('ticket_pk')
#         form.instance.ticket = Ticket.objects.get(id=ticket_pk)
#         return super().form_valid(form)
#
#
# class CommentDeleteView(DeleteView, LoginRequiredMixin):
#     template_name = 'comment/comment_delete.html'
#     model = Comment
#     success_url = reverse_lazy('comment_list')
#     login_url = reverse_lazy('user:login')

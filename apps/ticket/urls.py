from django.urls import path
from apps.ticket import views

urlpatterns = [
    path('', views.TicketView.as_view(), name='ticket_list'),
    path('create', views.TicketCreateView.as_view(), name='ticket_create'),
    path('update/<pk>', views.TicketUpdateView.as_view(), name='ticket_update'),
    path('delete/<pk>', views.TicketDeleteView.as_view(), name='ticket_delete'),
    path('<pk>', views.TicketDetailView.as_view(), name='ticket_detail'),

    path('<int:pk>/comment', views.CommentView.as_view(), name='comment_list'),
    path('<int:pk>/comment/create', views.CommentCreateView.as_view(), name='comment_create'),
    path('<int:pk>/comment/<int:comment_pk>/delete', views.CommentDeleteView.as_view(), name='comment_delete'),
]

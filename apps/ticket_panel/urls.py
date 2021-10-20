from django.urls import path
from apps.ticket_panel import views

urlpatterns = [
#    path('', views.TicketView.as_view(), name='ticket_list'),
    path('<int:pk>/status', views.StatusView.as_view(), name='ticket_panel_status'),
    path('', views.TicketView.as_view(), name='ticket_panel_list'),
    path('update/<pk>', views.TicketUpdateView.as_view(), name='ticket_panel_update'),
    path('<pk>', views.TicketDetailView.as_view(), name='ticket_panel_detail'),
]

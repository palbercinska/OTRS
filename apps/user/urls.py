from django.urls import path
from . import views
from .views import LoginView

app_name = 'user'

urlpatterns = [
    # path("", views.Homepage.as_view(), name="homepage"),
    path("", views.homepage, name="homepage"),
    path("register/", views.register_request, name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", views.logout_request, name="logout"),
]

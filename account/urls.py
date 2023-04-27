from django.urls import path

from .views import *

app_name = "account"

urlpatterns = [
    path("profile/", ProfileView.as_view(), name='profile'),
    path("logout/", CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/edit/', ProfileEditView.as_view(), name='edit')
]
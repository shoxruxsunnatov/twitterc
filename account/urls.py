from django.urls import path

from account import views

app_name = "account"

urlpatterns = [
    path("profile/", views.ProfileView.as_view(), name='profile'),
    path("logout/", views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/edit/', views.ProfileEditView.as_view(), name='edit')
]
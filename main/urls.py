from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.WelcomePage.as_view(), name='welcome'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('home/tweet/', views.AddTweet.as_view(), name='addtweet'),
    path('user/<str:username>/', views.AccountDetailView.as_view(), name='account_detail'),
    path('search/', views.SearchView.as_view(), name='search')
]
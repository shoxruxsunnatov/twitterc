from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('home/', views.TweetsBase.as_view()),
    path('profile/', views.ProfileTweets.as_view()),
    path('user/<int:account_id>/', views.TweetsBase.as_view()),
    path('search/<str:query>/', views.SearchView.as_view())
]
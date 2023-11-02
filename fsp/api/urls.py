from django.urls import path
from . import views

urlpatterns = [
    path('score', views.ScoreView.as_view()),
    path('posts', views.PostsView.as_view()),

]
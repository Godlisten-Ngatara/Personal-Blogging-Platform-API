from django.urls import path
from . import views
urlpatterns = [
    path('', views.getPosts),
    path('posts/<int:id>/', views.getPost),
    path('posts/add/', views.savePost)
]

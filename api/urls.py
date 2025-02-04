from django.urls import path
from . import views
urlpatterns = [
    path('posts/', views.getPosts),
    path('posts/<int:id>/', views.getPost),
    path('posts/add/', views.savePost),
    path('posts/<int:post_id>/updatePost', views.updatePost),
]

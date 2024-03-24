from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.blog_post_create, name='blog_post_create'),
    path('/', views.blog_post_list, name='blog_post_list'),
    path('doctor/', views.blog_post_list_doctor, name='blog_post_list_doctor'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
]

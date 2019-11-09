from django.urls import path
from .views import *

urlpatterns = [
    path('',PostListViews.as_view(),name='home'),
    path('user/<str:username>',UserPostListViews.as_view(),name='user-posts'),
    path('post/<int:pk>/',PostDetailViews.as_view(),name='post-detail'),
    path('post/new/',PostCreateViews.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateViews.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteViews.as_view(),name='post-delete'),
    path('about/',about,name='about'),
]

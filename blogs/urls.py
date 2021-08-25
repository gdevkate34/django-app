from django.urls import path
from blogs import views
from .views import (
    PostCreateView,PostUpdateView,PostDetailView,PostDeleteView
)

urlpatterns = [
    path('', views.home, name='blog_home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/detail/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
   
]

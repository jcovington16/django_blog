from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('blog/<int:pk>', views.PostDetailView.as_view(), name='blog_page'),
]

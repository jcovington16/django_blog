from django.views.generic import ListView, DetailView

from .models import Post 

class PostListView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    models = Post
    template_name = 'detail.html'
    context_object_name = 'cov'
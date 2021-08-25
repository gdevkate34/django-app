from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


# Create your views here.
def home(request):

    if request.method=="POST":
        post = Post(request.POST)
        post.save()



    context={
        'posts':Post.objects.all().order_by('-date_added'),
        'title':"Home"
    }
    if request.user.is_authenticated:
        return render(request,'blogs/home.html',context)
    else:
        return render(request,'blogs/home_cover.html',context)
    

class PostDetailView(LoginRequiredMixin,DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url ='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
   
        
    

from django.shortcuts import render
from django.urls import reverse_lazy 
from django.views import generic
from .forms import CustomUserCreationForm
from django.views.generic import ListView
from . models import Post
class SignUp(generic.CreateView): 
    form_class = CustomUserCreationForm 
    success_url = reverse_lazy('login') 
    template_name = 'signup.html'
class BlogListView(ListView): 
    model = Post 
    template_name = 'blog.html'
# Create your views here.

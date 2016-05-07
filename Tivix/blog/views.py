from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, UpdateView, DetailView, CreateView
# Create your views here.
from .models import Blog
from .forms import BlogForm

class BlogListView(ListView):
	'''
	this is the main page ListView of the blog
	'''
	model = Blog
	template_name = "blog/all.html"
	queryset = Blog.objects.all()

class BlogSingleView(DetailView):
	'''
	The DetailView of the blog
	'''
	model = Blog
	template_name = "blog/single.html" 


class BlogUpdateView(UpdateView):
	'''
	the UpdateView of the blog where all the edits go
	'''
	model = Blog
	fields = ['title', 'description']
	template_name ="blog/update_form.html"

class BlogCreateView(CreateView):
	template_name = "blog/forms.html"
	form_class = BlogForm



from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, UpdateView, DetailView
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


def blog_form(request):
	'''
	this is the functional Create View of the blog which takes
	data from the forms.py
	'''
	btn = 'submit'
	if request.method == "POST":
		form = BlogForm(request.POST or None)
		if form.is_valid():
			new_blog= form.save(commit=False)
			new_blog.save()
		return HttpResponseRedirect('/')
	else:
		form = BlogForm()

	template_name = "blog/forms.html"
	context = {
	"form":form,	
	"submit_btn": btn,
	}
	return render(request, template_name, context)

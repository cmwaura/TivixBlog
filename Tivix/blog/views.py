from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, UpdateView, CreateView, DetailView
# Create your views here.
from .models import Blog
from .forms import BlogForm

class BlogListView(ListView):
	model = Blog
	template_name = "blog/all.html"
	queryset = Blog.objects.all()

class BlogSingleView(DetailView):
	model = Blog
	template_name = "blog/single.html" 


class BlogUpdateView(UpdateView):
	model = Blog
	fields = ['title', 'description']
	template_name ="blog/update_form.html"


def blog_form(request):
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

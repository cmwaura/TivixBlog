from django import forms
from .models import Blog
from django.utils.text import slugify

class BlogForm(forms.ModelForm):
	'''
	Form for the user to create a blog
	'''
	description = forms.CharField(label="content (required)",
		widget=forms.Textarea(attrs={"size":40}),
		required=True)
	title = forms.CharField(label="Title (required)",
		widget =forms.TextInput(attrs={'size':40}),
		required=True)
	class Meta:
		model = Blog
		fields = ['title', 'description']

	def clean_title(self):
		title = self.cleaned_data.get('title')
		return title

	def clean_description(self):
		description = self.cleaned_data.get('description')
		return description

	def save(self, commit=True):
		blog = super(BlogForm, self).save(commit=False)
		blog.slug = slugify(blog.title)
		if commit:
			blog.save()
		return blog

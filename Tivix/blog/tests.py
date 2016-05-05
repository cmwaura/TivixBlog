from django.test import TestCase
# Create your tests here.
from django.utils.text import slugify
from .models import Blog
from .forms import BlogForm
'''
Testing the following.
1) models
2)views
3) forms
'''

class BlogModelsTestCase(TestCase):
	'''
	in this situation we aill be testing the __str__ test_string_rep
	in the models.py [passed]
	'''

	def test_string_rep(self):
		blog = Blog(title = "test title ")
		self.assertEqual(str(blog), blog.title)
	
	def test_get_absolute_url(self):
		blog = Blog.objects.create(title="my entry title", slug="entry-title")
		self.assertIsNotNone(blog.get_absolute_url())


class ProjectTest(TestCase):
	'''
	testing the homepage to see whether it passes
	[passed]
	'''
	def test_homepage(self):
		response = self.client.get("/")
		self.assertEqual(response.status_code, 200)

class HomePageTest(TestCase):
	'''
	Testing the list views in the HomePageTest
	[failed]
	'''
	def test_one_entry(self):
		Blog.objects.create(title="title-1", slug="title-1", description="description")
		response = self.client.get('/')
		self.assertContains(response, "title-1")
		# self.assertContains(response, s)
		self.assertContains(response, "description")
	# def test_two_entries(self):
	# 	Blog.objects.create(title="title-1", description="description")
	# 	Blog.objects.create(title="this is a title", description="description")
	# 	response = self.client.get('/')
	# 	self.assertContains(response, "title-1")
	# 	self.assertContains(response, "description")
	# 	self.assertContains(response, "this is a title")

# class BlogViewTest(TestCase):
# 	def setup(self):
# 		self.blog = Blog.objects.create(title="title", description="description")
	
# 	def test_basic_view(self):
# 		response = self.client.get(self.blog.get_absolute_url())
# 		self.assertEqual(response.status_code, 200)
	

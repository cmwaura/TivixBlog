from django.test import TestCase
# Create your tests here.
from django.utils.text import slugify
from django_webtest import WebTest
from .models import Blog
from .forms import BlogForm
from django.core.urlresolvers import reverse
'''
Testing the following.
1) models[done]
2)views[done]
3) forms[done]

code coverage
Name                                         Stmts   Miss  Cover
----------------------------------------------------------------
Tivix/__init__.py                                0      0   100%
Tivix/settings.py                               28      0   100%
Tivix/urls.py                                    7      0   100%
blog/__init__.py                                 0      0   100%
blog/admin.py                                    6      0   100%
blog/forms.py                                   21      0   100%
blog/migrations/0001_initial.py                  6      0   100%
blog/migrations/0002_auto_20160504_2122.py       5      0   100%
blog/migrations/__init__.py                      0      0   100%
blog/models.py                                  14      0   100%
blog/tests.py                                   85      0   100%
blog/views.py                                   18      0   100%
manage.py                                        6      0   100%
----------------------------------------------------------------
TOTAL                                          196      0   100%


'''

class BlogModelsTestCase(TestCase):
	'''
	in this situation we aill be testing the __str__ test_string_rep
	in the models.py [passed]
	'''

	def test_string_repr(self):
		blog = Blog(title = "test title ")
		self.assertEqual(str(blog), blog.title)
	
	def test_get_absolute_url(self):
		'''
		Testing for the get_absolute_url function defined in the models.py
		'''

		blog = Blog.objects.create(title="my entry title", slug="entry-title")
		self.assertIsNotNone(blog.get_absolute_url())


class ProjectTest(TestCase):
	'''
	testing the homepage url to see whether it passes
	[passed]
	'''
	def test_homepage(self):
		response = self.client.get("/")
		self.assertEqual(response.status_code, 200)

class HomeListViewTest(WebTest):
	'''
	Testing the list views in the HomePageTest
	[passed]
	'''
	
	def test_one_blog(self):
		'''
		This is testing just one entry on the home page 
		'''
		Blog.objects.create(title="title-1", slug="title-1", description="description")
		response = self.client.get('/')
		self.assertContains(response, "title-1")		
		self.assertContains(response, "description")
	def test_two_blogs(self):
		'''
		Since this is a list view, its also better to test two entries.
		'''
		Blog.objects.create(title="Second entry", slug= "second-entry", description="description")
		Blog.objects.create(title="this is a title",slug= "this-title", description="description")
		response = self.client.get('/')
		self.assertContains(response, "Second entry")
		self.assertContains(response, "description")
		self.assertContains(response, "this is a title")
	
	def test_no_blog(self):
		'''
		checks to see in case there are no blogs available. This is done via the empty tag
		in the templates at all.html
		'''
		response = self.client.get('/')
		self.assertContains(response, 'sorry, there are no blogs currently available')

class BlogUpdateviewTest(WebTest):
	'''
	testing the update view in the blog.views
	'''

	def test_update_view(self):
		'''
		Sanity check
		'''
		blog = Blog.objects.create(title="Second entry", slug= "second-entry", description="description")
		response = self.client.get(reverse('update_blog', args=[blog.slug]))
		self.assertEqual(response.status_code, 200)
		self.assertTrue('form' in response.content)
	
	def test_blog(self):		
		blog = Blog.objects.create(title="Second entry", slug= "second-entry", description="description")
		
		update_data = reverse('update_blog', args=[blog.slug])
		# we ger the form to update the objects
		response = self.client.get(update_data)
		form =  response.context['form']
		data = form.initial
		# Lets change the title and description

		data = {
		'title': 'test',		
		'description': 'update description'
		}
		# POST the form with the changed data
		r = self.client.post(update_data, data)
		# now lets retrieve our objects to see whether we have changed them

		response = self.client.get(update_data)
		# see if it contains the new title from data['title']=test
		self.assertContains(response, 'test')
		# see if it contains the description 
		self.assertEqual(response.context['form'].initial['description'], 'update description')

class BlogDetailViewTest(WebTest):
	'''
	This class is mainly for testing the description and title in the single 
	setup where a user can actually read the articles. It uses the get_absolute_url
	defined in the models.py [passed]
	'''
	def setUp(self):
		self.blog = Blog.objects.create(title="title", slug="title-django", description="description")
	
	def test_basic_view(self):
		'''
		it checks the blog and uses the client to get the response status_code then 
		verifies that it is equal to 200
		'''
		response = self.client.get(self.blog.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_title_in_blog(self):
		response = self.client.get(self.blog.get_absolute_url())
		self.assertContains(response, self.blog.title)

	def test_description_in_blog(self):
		response = self.client.get(self.blog.get_absolute_url())
		self.assertContains(response, self.blog.description)

class BlogCreateView(WebTest):

	def test_create_view(self):
		'''
		Sanity check
		'''
		blog = Blog(title="Second entry", slug= "second-entry", description="description")
		response = self.client.get(reverse('blog_form'))
		self.assertEqual(response.status_code, 200)
		self.assertTrue('form' in response.content)
		data = {
		'title': 'test',		
		'description': 'update description'
		}
		# POST the form with the created data
		r = self.client.post(reverse('blog_form'), data)
		# now lets retrieve our objects to see whether we have created them

		blog = Blog.objects.order_by('created_date').first()
		# # see if it contains the new title from data['title']=test
		self.assertContains(response, 'test')
		# # see if it contains the description 
		self.assertEqual(blog.title, 'test')
		self.assertEqual(blog.description, data['description'])

	

class BlogFormTest(WebTest):
	'''
	Testing the forms of the blog
	'''
	
	def test_valid_data(self):
		'''
		Test the data we place in and see if it is equal to the actual data
		'''
		form = BlogForm({
			'title': "nice title",
			'description':'this is a description'
			})
		self.assertTrue(form.is_valid())
		blog = form.save()
		self.assertEqual(blog.title, "nice title")
		
		self.assertEqual(blog.description, "this is a description")
	
	def test_blank_data(self):
		form = BlogForm({})
		self.assertFalse(form.is_valid())
		self.assertEqual(form.errors,{			
			'title': [u'This field is required.'],			
			'description':[u'This field is required.']
			})
	

from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Blog(models.Model):
	'''
	the blog model containing the title, description and DateTimeField
	'''
	title = models.CharField(max_length=140)
	description = models.TextField(max_length=2000)
	created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	slug = models.SlugField(unique=True)

	def __str__(self):
		return self.title

	class Meta:
		unique_together = ("title", "slug",)

	def get_absolute_url(self):
		return reverse('single_blog', kwargs={'slug':self.slug})
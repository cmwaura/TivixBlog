from django.contrib import admin

from .models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
	''' 
	Admin page with list_display which contains the title and created_date
	prepopulated_fields will populate the field as per the title of the Blog
	'''
	list_display = ("__str__", "created_date")
	prepopulated_fields = {"slug":("title",)}


admin.site.register(Blog, BlogAdmin)
from django.contrib import admin

from .models import Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
	list_display = ("__str__", "created_date")
	prepopulated_fields = {"slug":("title",)}
admin.site.register(Blog, BlogAdmin)
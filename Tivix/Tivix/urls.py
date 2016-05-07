"""Tivix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from blog.views import BlogListView as blog_list
from blog.views import BlogSingleView as blog_single
from blog.views import BlogCreateView as blog_form
from blog.views import BlogUpdateView as blog_update

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # blog app urls that map the view to template.

    url(r'^$', blog_list.as_view(), name='blog'),
    url(r'blog/create/$', blog_form.as_view(), name='blog_form'),
    url(r'^blog/(?P<slug>[\w-]+)/$', blog_single.as_view(), name='single_blog'),
    url(r'^blog/update/(?P<slug>[\w-]+)/$', blog_update.as_view(), name='update_blog'),


]


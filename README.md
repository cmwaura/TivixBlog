# TivixBlog
This is a small miniature blog that was done with django with the database being PostgreSQL

In this documentation, It will be explained as to the process i took in completing this project. 
However, concise(einstein) code documentation is present within the code.

### APP
##### Models.py
created the model as per requested with the "title", "Created_date" and "description". Added an extra
field "slug" for the detail blog mapping.

slug and title are unique together.

##### Admin.py

Contains BlogAdmin which oversees the population of the slug via the prepopulated fields as well as  has
the list display on the title and created date.

##### Forms.py 
contains the forms where a client can create a blog.
In addition to the form, It cleans all the input so as to protect any harmful data from getting to the backend
portion.

##### views.py
Contains the following:
###### BlogListView(ListView)
This is the blog list view that is mapped to the home page.

###### BlogSingleView(DetailView)
This is the view that ensures that the user can actually read each individual post. In addition to that it is important
to note that this view requires the get_absolute_url method which is displayed on the model. It uses the key word arg of 
a dict{ 'slug': self.slug}

###### BlogUpdateView(UpdateView):
This is the edit portion of the app that when activated allows the user to edit their posts

###### blog_form(request)
this view is responsible for processing the BlogForm from forms.py. It Checks whether the request method is POST and
if the form is_valid() it saves the form and goes to the homepage.

### Templates
##### Base.html
base file of the templates which contains all the bootstrap CDN's. 
##### Blog
Contains:
  all.html - home page and the list view of all the blogs
  
  single.html - single detail template of the blog
  
  forms.html - forms for creating the blog as well as updating it.

### Settings.py
Created a Cache at the backend to save persistent post data from the posts.



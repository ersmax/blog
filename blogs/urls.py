"""Define URL patterns for blogs"""

from django.urls import path    # path to map URLs to views
from . import views             # views to process data and render a page

app_name = 'blogs'              # namespace of this app
urlpatterns = [                 # list of urls that can be requested from blogs app
    # Home page
    path('', views.index, name='index'),
    # Page to view all the blogs that have been created
    path('blogs/', views.blogs, name='blogs'),
    # Page to view an individual blog and its posts
    path('blog/<int:blog_id>/', views.blog, name='blog'),
    
    # Page to create new blog
    path('new_blog/', views.new_blog, name='new_blog'),
    # Page to create a new post
    path('new_post/<int:blog_id>/', views.new_post, name='new_post'),
    # Page for editing a post
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]

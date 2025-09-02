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
]

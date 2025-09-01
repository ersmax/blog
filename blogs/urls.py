"""Define URL patterns for blogs"""

from django.urls import path    # path to map URLs to views
from . import views             # views to process data and render a page

app_name = 'blogs'              # namespace of this app
urlpatterns = [                 # list of urls that can be requested from blogs app
    # Home page
    path('', views.index, name='index'),
]

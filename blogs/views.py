from django.shortcuts import render
from .models import Blog

# Create your views here.
def index(request):
    """The homepage for blog"""
    return render(request, 'blogs/index.html')

def blogs(request):
    """Page to view all blogs that have been newly creted"""
    blogs = Blog.objects.order_by('name')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)


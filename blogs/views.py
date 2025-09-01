from django.shortcuts import render

# Create your views here.
def index(request):
    """The homepage for blog"""
    return render(request, 'blogs/index.html')
from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm, BlogPostForm

# Create your views here.
def index(request):
    """The homepage for blog"""
    return render(request, 'blogs/index.html')

def blogs(request):
    """Page to view all blogs that have been newly creted"""
    blogs = Blog.objects.order_by('name')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    """Page to view a specific blog and its posts"""
    blog = Blog.objects.get(id=blog_id)
    posts = blog.blogpost_set.order_by('-date_added') # reverse lookup <modelname>_set
    context = {'blog': blog, 'posts': posts}
    return render(request, 'blogs/blog.html', context)

def new_blog(request):
    """Page to a new blog. Initial request of a blank form."""
    """Subsequent processing of data submitted in the form."""
    if request.method != 'POST':
        # create a blank form
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)      # pass the data requested by user through request.POST
        if form.is_valid():         # check all fields have been filled in
            form.save()             # save data to db
            return redirect('blogs:blogs')  # redirect to view of blogs

    # Display a blank or invalid form
    context  = {'form':form}
    return render(request, 'blogs/new_blog.html', context)

def new_post(request, blog_id):
    """Page to create a new post"""
    blog = Blog.objects.get(id=blog_id)

    if request.method != 'POST':
        # No data submitted, hence create a blank entry
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)      # pass the data requested by user through request.POST
        if form.is_valid():
            new_post = form.save(commit = False)   # do not save yet to db
            new_post.blog = blog
            new_post.save()
            return redirect('blogs:blog', blog_id=blog_id)  # redirect to the specifc blog_id with all its entries
    
    # Display a blank form or invalid form in case info is missing
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/new_post.html', context)



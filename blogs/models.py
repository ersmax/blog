from django.db import models

# Create your models here: 
# a model tell Django how to work with data
# what will be stored in the app
class Blog(models.Model):
    """A person or organization's blog"""
    date_added = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        """Format the output string for the blog"""
        return self.name
    
class BlogPost(models.Model):
    """Represent a single post in the blog"""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)    # if a blog gets deleted, all the posts will be too
    
    title = models.CharField(max_length=500)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Format the output string for the post"""
        if len(self.title) < 50:
            return self.title
        return f"{self.title[:50]}..."

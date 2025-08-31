from django.db import models

# Create your models here: 
# a model tell Django how to work with data
# what will be stored in the app
class Blog(models.Model):
    """A person or organization's blog"""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Format the output string"""
        return self.name
    
class BlogPost(models.Model):
    """Represent a single blog post"""

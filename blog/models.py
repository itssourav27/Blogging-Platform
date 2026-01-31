from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify 
import math 
from django.conf import settings


class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True ,blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/',blank=True,null =True )
    tags = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def reading_time(self):
        words = self.content.split()
        word_count = len(words)
        minutes = math.ceil(word_count / 200)
        return minutes
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title
        
        

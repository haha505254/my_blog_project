from django.db import models
from django.contrib.auth.models import User
from uuid import uuid1
from django.urls import reverse
# Create your models here.


class Post(models.Model):


    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,default=uuid1,unique=True)
                          
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # image = models.ImageField(upload_to='images',blank=True,null=True)


    

    
    def __str__(self):
        return self.title

    def get_url(self):
        return reverse(
            'post_detail',
            args=[
                self.slug,
            ]
        )
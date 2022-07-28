from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):


    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
                          
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images',blank=True,null=True)
    
    class Meta:
        unique_together = ('slug', 'author',)
    
    def __str__(self):
        return self.title
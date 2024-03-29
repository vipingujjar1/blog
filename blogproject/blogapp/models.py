from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICE=(('draft','Draft'),('published','Published'))
    title=models.CharField(max_length=260)
    slug=models.SlugField(max_length=264,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=20,choices=STATUS_CHOICE,default='draft')

    objects=CustomManager()

    class Meta:
        ordering=('-publish',)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comment', on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

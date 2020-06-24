from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,  self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User,related_name='posts', on_delete=models.CASCADE)
    body = models.TextField()
    thumb = models.ImageField(default='default.png', blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


    objects = models.Manager()  # The default manager
    published = PublishedManager() # our custom manager
    tags = TaggableManager()
    
    def get_absolute_url(self):
        return reverse('poems:post_detail', args=[self.publish.year,
                                                    self.publish.month,
                                                    self.publish.day,
                                                    self.slug])
    

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
        


class Photo(models.Model):
    author = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    info = models.CharField(max_length=100)
    slug = models.SlugField(default='detail-view')
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)

    def show_img(self):
        return self.author

    def __str__(self):
        return self.info[:100] + '...'

class Poem(models.Model):
    author = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    actual_owner = models.CharField(max_length=80, default='author')
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def content(self):
        return self.body



    



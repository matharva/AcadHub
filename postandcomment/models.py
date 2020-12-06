from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

# Create your models here.

class Community(models.Model):
    name = models.CharField(max_length=200, default='SomeName')
    description = models.CharField(max_length=400, blank=True)
    user = models.ManyToManyField(User)
    
class Post(models.Model):
    content = models.TextField(default="testContent")
    title = models.TextField(default="testPost")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='post_pics', blank = True)
    upvote = models.PositiveIntegerField(default=0)
    downvote = models.PositiveIntegerField(default=0)
    category = models.CharField(default='global', max_length=200)
    link = models.URLField(blank = True)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.author.username} Post- {self.title}'

    def save(self, *args, **kwargs): 
        super().save(*args, **kwargs) 
        img = Image.open(self.image.path) 
        if img.height > 400 or img.width > 400: 
            output_size = (300, 300) 
            img.thumbnail(output_size) 
            img.save(self.image.path)
    

class Comment(models.Model): 
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name ='comments') 
    user = models.ForeignKey(User, on_delete = models.CASCADE) 
    content = models.TextField() 
    date = models.DateTimeField(default=timezone.now)
    upvotes = models.PositiveIntegerField(default=0)



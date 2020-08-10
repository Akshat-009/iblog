from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.
class Query(models.Model):
    name = models.CharField(max_length=128)
    email=models.EmailField()
    query = models.TextField()

    def __str__(self):
        return self.name
class PostCategory(models.Model):
    category = models.CharField(max_length=12)
    def __str__(self):
        return self.category
class Post(models.Model):
    id=models.AutoField(primary_key=True)
    author= models.CharField(max_length=122)
    category=models.ForeignKey(PostCategory,on_delete=models.CASCADE)
    title = models.CharField(max_length=122)
    content=models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    slug=models.SlugField(null=True,blank=True)
    def save(self):
        self.slug=slugify(self.title)
        super(Post, self).save()
    def __str__(self):
        return self.title
class BlogComment(models.Model):
    id=models.AutoField(primary_key=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    comment=models.TextField()
    parent=models.ForeignKey('self',blank=True,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.comment[0:12]

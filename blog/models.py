from django.db import models

# Create your models here.
class Query(models.Model):
    name = models.CharField(max_length=128)
    email=models.EmailField()
    query = models.TextField()

    def __str__(self):
        return self.name
class PostCategory(models.Model):
    category = models.CharField(max_length=12)
class Post(models.Model):
    category=models.ForeignKey(PostCategory,on_delete=models.CASCADE)
    title = models.CharField(max_length=122)
    content=models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    slug=models.CharField(max_length=122)
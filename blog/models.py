from django.db import models

# Create your models here.
class Query(models.Model):
    name = models.CharField(max_length=128)
    email=models.EmailField()
    query = models.TextField()

    def __str__(self):
        return self.name
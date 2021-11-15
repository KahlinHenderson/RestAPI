from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    date = models.DateField(default=timezone.now)
    author = models.CharField(max_length=200)
    post_image = models.ImageField(blank=True, upload_to='photos/%Y/%m')

    def __str__(self):
        return self.title

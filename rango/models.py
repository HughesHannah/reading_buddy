from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import datetime

# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=128, unique=True)

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.cat_name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.cat_name

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=128, unique=True)
    author = models.CharField(max_length=128)
    intro = models.TextField()
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    score = models.FloatField() 

    slug = models.SlugField(unique = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.book_name)
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.book_name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateField(auto_now=datetime.datetime.now())

    def __str__(self):
        return self.content

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class ReadingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username






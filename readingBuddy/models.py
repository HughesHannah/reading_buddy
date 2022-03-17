from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import datetime


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
    #readinglist = models.ForeignKey(ReadingList, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=128, unique=True)
    author = models.CharField(max_length=128)
    intro = models.TextField()
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    score = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    slug = models.SlugField(unique = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.book_name)
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.book_name

class Comment(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateField(auto_now=datetime.datetime.now())

    def __str__(self):
        return self.content
        

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance. 
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # The additional attributes we wish to include. 
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

class ReadingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #book_name = models.ForeignKey(Book, on_delete=models.CASCADE)
    book1= models.CharField(max_length=128, unique=True)
    book2= models.CharField(max_length=128, unique=True)
    book3= models.CharField(max_length=128, unique=True)
    book4= models.CharField(max_length=128, unique=True)
    book5= models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.user.username






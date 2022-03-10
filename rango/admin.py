from django.contrib import admin

from rango.models import Category, Book, Comment, ReadingList

# Register your models here.

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(ReadingList)

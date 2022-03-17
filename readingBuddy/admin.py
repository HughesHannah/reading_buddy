from django.contrib import admin 
from readingBuddy.models import Category, Book, Comment, ReadingList, UserProfile

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('cat_name',)}   

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(ReadingList)
admin.site.register(UserProfile)


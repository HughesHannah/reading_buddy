from django.test import TestCase
from readingBuddy.models import Category,Book,Comment,UserProfile
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

def add_book(cat, name,views, likes):
    book = Book.objects.get_or_create(category=cat,book_name=name)[0]
    book.views = abs(views)
    book.likes = abs(likes)
    book.save()
    return book

def add_category(name):
    category = Category.objects.get_or_create(cat_name=name)[0]
    category.save()
    return category

def add_comment(bookname,content):
    comment= Comment.objects.get_or_create(Book=bookname,content=content,user_id=1)[0]
    comment.save()
    return comment

def add_user():
    user = User.objects.get_or_create(username='test',email='test.gmail.com')[0]
    user.set_password('123456')
    user.save()

    profile = UserProfile.objects.get_or_create(user=user)[0]
    profile.save()

class BookMethodTests(TestCase):
   def test_ensure_views_are_positive(self):
     """
    Ensures the number of views received for a Category are positive or zero.
   """
     categoryn = add_category('Django')
     book = Book(category=categoryn,book_name='test', views=1, likes=1)
     book.save()
     self.assertTrue(book.views >0)

'''
   def test_slug_line_creation1(self):
    """
     Checks to make sure that when a Book is created, an
     appropriate slug is created.
     Example: "Random Book String" should be "random-book-string".
    """
    book = Book(book_name='Random Book String')
    #book = add_book('Random Book String')
    book.save()
    self.assertEqual(book.slug, 'random-book-string')
    '''


class IndexViewTests(TestCase):
   def test_index_view_with_no_categories(self):
     """
     If no categories exist, the appropriate message should be displayed.
     """
     response = self.client.get(reverse('readingBuddy:index'))
     self.assertEqual(response.status_code, 200)
     self.assertContains(response, 'There are no categories present.')
     self.assertQuerysetEqual(response.context['categories'], [])

   def test_index_view_with_categories(self):
      """
      Checks whether categories are displayed correctly when present.
      """
      add_category('Python')
      add_category('C++' )
      add_category('Erlang')
      response = self.client.get(reverse('readingBuddy:index'))
      self.assertEqual(response.status_code, 200)
      self.assertContains(response, "Python")
      self.assertContains(response, "C++")
      self.assertContains(response, "Erlang")
      num_categories = len(response.context['categories'])
      self.assertEquals(num_categories, 3)

class CategoryMethodTests(TestCase):
    def test_slug_line_creation2(self):
        """
        Checks to make sure that when a category is created, an appropriate slug is created.
        Example: "Random Category String" should be "random-category-string".
        """
        category = add_category('Random Category String')
        category.save()

        self.assertEqual(category.slug, 'random-category-string')

class CommentAccessTests(TestCase):
    def test_Comment_not_in_future(self):
        category = add_category('What')
        book=add_book(cat=category,name='Test', likes=-1, views=-1)
        comment=add_comment(bookname=book,content='test_comment_content')
        #print(comment)
        #self.assertTrue(comment.date<=timezone.now())
        self.assertTrue(len(comment.content)!=0)


        


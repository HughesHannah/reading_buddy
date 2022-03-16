from django.shortcuts import render

from rango.models import Book
from rango.models import Category, Comment

# Create your views here.
def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        books = Book.objects.filter(category=category)
        most_view = Book.objects.order_by('-views')[:5]


        context_dict['category'] = category
        context_dict['books'] = books
        context_dict['most_view'] = most_view
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['books'] = None
        context_dict['most_view'] = None
    return render(request, 'rango/category.html', context=context_dict)


@login_required
def books(request):
    category_list = Category.objects.order_by('-likes')[:5]
    books_list = Book.objects.order_by('score')[:5]

    context_dict = {}
    context_dict['categories'] = category_list
    context_dict['books'] = books_list

    return render(request, 'rango/book.html', context=context_dict)

@login_required
def search_do(request):
    search_item = request.GET.get('search')
    current_user = request.user
    book_list = Book.objects.filter(user= current_user,title__icontains=search_item)
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict['current_page'] = search_item
    context_dict['categories'] = category_list
    context_dict['books'] = book_list


    return render(request, 'rango/searchpage.html', context=context_dict)
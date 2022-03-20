from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.urls import reverse
from readingBuddy.models import Category, Book, Comment, UserProfile, ReadingList
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from readingBuddy.forms import UserForm, UserProfileForm, CommentForm
from django.views.decorators.csrf import csrf_exempt


###############################################################


############################ index ############################
## [test result] 
#   - category_list, book_list, most_popular show on the webpage of index_test.html
#   - the static file (picture) shows on the webpage of index_test.html
#   (comment by Yifan)
def index(request):
    categories = Category.objects.all()
    books = Book.objects.all()
    most_popular = Book.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict['categories'] = categories
    context_dict['books'] = books
    context_dict['most_popular'] = most_popular

    visitor_cookie_handler(request)

    #return render(request, 'readingBuddy/index_test.html', context=context_dict)
    return render(request, 'readingBuddy/index.html', context=context_dict)

############################ about ############################
## [test result] 
#  - visits can shows on http://127.0.0.1:8000/readingBuddy/about/
def about(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    return render(request, 'readingBuddy/about.html', context=context_dict)


############################ visitor_cookie_handler ############################
# A helper method
def get_server_side_cookie(request, cookie, default_val=None): 
    val = request.session.get(cookie)
    if not val:
        val = default_val 
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie
    
    request.session['visits'] = visits

############################ show category ############################
## [test result] 
#   - can show related books in specified category
def show_category(request, category_name_slug):
    context_dict = {}

    try:
        categories = categories = Category.objects.all()
        category = Category.objects.get(slug=category_name_slug)
        books = Book.objects.filter(category=category).order_by('-likes')[:5]

        context_dict['categories'] = categories
        context_dict['category'] = category
        context_dict['books'] = books
    except Category.DoesNotExist:
        context_dict['categories'] = None
        context_dict['category'] = None
        context_dict['books'] = None
    return render(request, 'readingBuddy/category.html', context=context_dict)


############################ book page - show book's info & comment ############################
## [test result] 
#   - can show books & related comments
def show_book(request, book_name_slug):
    context_dict = {}

    try:
        categories = categories = Category.objects.all()
        book = Book.objects.get(slug=book_name_slug)
        comments = Comment.objects.filter(Book=book)

        context_dict['categories'] = categories
        context_dict['book'] = book
        context_dict['comments'] = comments
    except Book.DoesNotExist:
        context_dict['categories'] = None
        context_dict['book'] = None
        context_dict['comments'] = None

    return render(request, 'readingBuddy/book.html', context=context_dict)
    

############################ register ############################
## [test result] 
#   - simple form shows on the http://127.0.0.1:8000/readingBuddy/register/  
#   - pay attention: the return path is linked to register_test.html
#   - regist function test successfully - register success!
#       - need to click href to jump to index page
## ！！！！pay attention！！！！！:  return path is linked to register_test.html 
#  > "register_test.html" is added to test whether the form and the function can run successfully
#  > You have to modify and test the register.html by changing the view's return address to register.html
#  (comment by Yifan)

def register(request):
    categories = Category.objects.all()
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'readingBuddy/register.html', context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered, 'categories': categories})

############################ user_login ############################
## [test result] 
#   - login successful, jump to index page
 
def user_login(request):
    context_dict = {}
    categories = Category.objects.all()
    context_dict['categories'] = categories

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('readingBuddy:userpage'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'readingBuddy/login.html', context=context_dict)

############################ restricted ############################
@login_required
def restricted(request):
    context_dict = {}
    categories = Category.objects.all()
    context_dict['categories'] = categories

    return render(request, 'readingBuddy/restricted.html', context=context_dict)

############################ user_logout ############################
@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('readingBuddy:index'))

############################# userpage ############################
## [test result] 
#   - succesfully show content
@login_required
def userpage(request):
    categories = Category.objects.all()
    comments = Comment.objects.filter(user=request.user)
    readlist_list = ReadingList.objects.all()
    # book_list = Book.objects.filter(user=request.user) # future function

    context_dict = {}
    context_dict['categories'] = categories
    context_dict['readlist_list'] = readlist_list
    context_dict['comments'] = comments

    visitor_cookie_handler(request)
    return render(request, 'readingBuddy/userpage.html', context=context_dict)


############################ add_comment ############################
## [test result] 
#   - succesfully add & show comment
@login_required
@csrf_exempt
def add_comment(request, book_name_slug):
    context_dict = {}
    try:
        book = Book.objects.get(slug=book_name_slug)
        comments = Comment.objects.filter(Book=book)

        context_dict['book'] = book
        #context_dict['comments'] = comments
    except:
        context_dict['book'] = None
        context_dict['comments'] = None
    
    # You cannot add a comment to a book that does not exist...
    if book is None:
        return redirect('/readingBuddy/')
    
    form = CommentForm()

    if request.POST:
        form = CommentForm(request.POST)

        if form.is_valid():
            content = request.POST.get('content')
            obj = Comment(
                Book=book,
                user=request.user,
                content=content,
                #date
            )
            obj.save()
            return redirect(reverse('readingBuddy:show_book', kwargs={'book_name_slug': book_name_slug}))

        else:
            print(form.errors)
    if not request.user.is_authenticated:
        return redirect(reverse('readingBuddy:login'))
    context_dict['form'] = form
    context_dict['comments'] = comments
    return render(request, 'readingBuddy/book.html', context=context_dict)


############################ search_do  ############################
## [test result] 
#   - can show the search result
def search_do(request):
    search_item = request.GET.get('search')
    current_user = request.user
    book_list = Book.objects.filter(book_name__icontains=search_item)
    categories = Category.objects.all()
    context_dict = {}
    context_dict['current_page'] = search_item
    context_dict['categories'] = categories
    context_dict['books'] = book_list

    return render(request, 'readingBuddy/searchpage.html', context=context_dict)


############################ add_wishlist  ############################
## [test result] 
#   - successfully add book_name to reading list
@login_required
def add_wishlist(request):
    current_user = request.user
    book_name = request.GET.get('book_name')

    reading_list = ReadingList.objects.get(user = current_user)

    reading_list.book1 = book_name

    reading_list.save()

    messages.info(request, 'The book has added to your wishlist')

    return render(request, 'readingBuddy/book.html')


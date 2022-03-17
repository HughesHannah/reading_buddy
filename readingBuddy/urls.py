from django.urls import path 
from readingBuddy import views

app_name = 'readingBuddy'

urlpatterns = [ 
	path('', views.index, name='index'), 
    path('about/', views.about, name="about"),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),
    path('userpage/', views.userpage, name='userpage'),
    path('search_do/', views.search_do, name="search"),
]
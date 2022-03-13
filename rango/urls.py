from django.contrib import admin 
from django.urls import path
from django.urls import include
from rango import views

urlpatterns = [ 
	path('', views.index, name='index'),
	path('rango/', include('rango.urls')),
	# 上面代码映射了任何以rango/开头的url，由rango处理
	path('admin/', admin.site.urls),
]
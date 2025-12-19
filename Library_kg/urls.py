from django.contrib import admin
from django.urls import path, include
from books import views as book_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_views.home, name='home'),
    path('books/', include('books.urls')),
    path('auth/', include('registration.urls')),
    path('captcha/', include('captcha.urls')),
    path('shop/', include('products.urls')), 
]
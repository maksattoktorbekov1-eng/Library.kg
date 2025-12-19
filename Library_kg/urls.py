from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('auth/', include('registration.urls')),   
    path('shop/', include('products.urls')),
    path('captcha/', include('captcha.urls')),     
]

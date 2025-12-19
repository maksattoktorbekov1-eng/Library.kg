from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.product_add, name='product_add'),
    path('<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('search/', views.search_products, name='search_products'),
    path('men/', views.category_products, {'category_name': 'men'}, name='men_products'),
    path('women/', views.category_products, {'category_name': 'women'}, name='women_products'),
    path('kids/', views.category_products, {'category_name': 'kids'}, name='kids_products'),
    path('cart/', views.cart_view, name='cart'),]
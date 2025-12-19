from django.urls import path
from .views import (
    ProductListView, CategoryProductsView,
    ProductCreateView, ProductUpdateView, ProductDeleteView,
    SearchProductsView, CartView
)

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('category/<str:category_name>/', CategoryProductsView.as_view(), name='category_products'),
    path('add/', ProductCreateView.as_view(), name='product_add'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('search/', SearchProductsView.as_view(), name='search_products'),
    path('cart/', CartView.as_view(), name='cart_view'),
]

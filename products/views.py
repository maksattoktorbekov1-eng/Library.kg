from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import redirect
from .models import Product
from .forms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

class CategoryProductsView(ListView):
    model = Product
    template_name = 'products/category.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_name = self.kwargs.get('category_name')
        return Product.objects.filter(category=category_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_name = self.kwargs.get('category_name')
        context['category_name'] = dict(Product._meta.get_field('category').choices).get(category_name, '')
        return context

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('product_list')

class SearchProductsView(ListView):
    model = Product
    template_name = 'products/search_results.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

class CartView(TemplateView):
    template_name = 'products/cart.html'

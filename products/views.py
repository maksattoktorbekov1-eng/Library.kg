from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from django.db.models import Q

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def category_products(request, category_name):
    products = Product.objects.filter(category=category_name)
    category_display = dict(Product._meta.get_field('category').choices).get(category_name, '')
    return render(request, 'products/category.html', {
        'products': products,
        'category_name': category_display
    })

def product_add(request):
    form = ProductForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'products/product_form.html', {'form': form})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'products/product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_delete.html', {'product': product})

def search_products(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query)
    )
    return render(request, 'products/search_results.html', {'products': products, 'query': query})
def cart_view(request):
    return render(request, 'products/cart.html')

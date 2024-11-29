from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from users.models import College
from .forms import ProductForm
from decimal import Decimal
# products/views.py (add this to your existing views)
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden

@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    # Check if the logged-in user is the owner of the product
    if product.seller != request.user:
        return HttpResponseForbidden("You don't have permission to delete this product.")
    
    if request.method == 'POST':
        # Delete the product
        product.delete()
        messages.success(request, 'Product successfully deleted.')
        return redirect('my_products')
    
    return render(request, 'products/confirm_delete.html', {'product': product})

@login_required
def my_products(request):
    """Display the products that the logged-in user has added."""
    products = Product.objects.filter(seller=request.user)
    
    query = request.GET.get('q')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    
    # Apply search filter
    if query:
        products = products.filter(title__icontains=query)
    
    # Apply price filter
    if min_price:
        try:
            min_price = Decimal(min_price)
            products = products.filter(price__gte=min_price)
        except (ValueError, Decimal.InvalidOperation):
            pass
    
    if max_price:
        try:
            max_price = Decimal(max_price)
            products = products.filter(price__lte=max_price)
        except (ValueError, Decimal.InvalidOperation):
            pass
    
    context = {
        'products': products,
        'query': query,
        'min_price': min_price,
        'max_price': max_price
    }
    
    return render(request, 'products/my_products.html', context)

@login_required
def product_list(request):
    """Display the list of all products with optional filtering."""
    query = request.GET.get('q')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    college_id = request.GET.get('college')  # Get college filter from request

    products = Product.objects.all()

    # Apply search filter
    if query:
        products = products.filter(title__icontains=query)

    # Apply price filter
    if min_price:
        try:
            min_price = Decimal(min_price)
            products = products.filter(price__gte=min_price)
        except (ValueError, Decimal.InvalidOperation):
            pass

    if max_price:
        try:
            max_price = Decimal(max_price)
            products = products.filter(price__lte=max_price)
        except (ValueError, Decimal.InvalidOperation):
            pass

    # Apply college filter if selected
    if college_id:
        products = products.filter(seller__college_id=college_id)

    colleges = College.objects.all()

    context = {
        'products': products,
        'query': query,
        'min_price': min_price,
        'max_price': max_price,
        'colleges': colleges,
        'selected_college': college_id
    }

    return render(request, 'products/product_list.html', context)

@login_required
def create_product(request):
    """Allow a user to create a new product and automatically link it to their college."""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.college = request.user.college  # Link product to seller's college
            product.save()
            return redirect('my_products')
    else:
        form = ProductForm()
    
    context = {'form': form}
    return render(request, 'products/create_product.html', context)

@login_required
def product_detail(request, pk):
    """Display the details of a specific product."""
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

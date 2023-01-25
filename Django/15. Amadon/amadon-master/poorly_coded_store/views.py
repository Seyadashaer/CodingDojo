from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()

    }
    return render(request, "store/index.html", context)

def checkout_process(request):
    product_id = request.POST["product_id"] 
    product = Product.objects.get(id=product_id)

    quantity = int(request.POST["quantity"])
    price = float(product.price)
    total_price = quantity * price

    Order.objects.create(quantity_ordered=quantity, total_price=total_price)
    return redirect('/checkout')

def checkout(request):
    context = {
        "most_recent_order": Order.objects.latest('id')
    }
    return render(request, "store/checkout.html", context)

from django.shortcuts import render, get_object_or_404, redirect
from services.models import ServicesProduct
from .models import Cart


# Create your views here.
def cart(request):
    all_cart_items = Cart.objects.all()
    error = ''
    if len(all_cart_items) == 0:
        error = "Your Cart is Empty!!"

    return render(request, 'cart.html', {'all_cart_items': all_cart_items, 'error': error})


def add_to_cart(request, product_id):
    product = get_object_or_404(ServicesProduct, pk=product_id)
    new_cart_item = Cart()
    new_cart_item.title = product.title
    new_cart_item.image = product.image
    new_cart_item.prices = product.prices
    new_cart_item.save()
    return redirect('services')


def delete_item(request, product_id):
    product = get_object_or_404(Cart, pk=product_id)
    Cart.delete(product)
    return redirect('cart')

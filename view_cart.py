from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from menu.models import MenuItem

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/view_cart.html', {'cart': cart})

@login_required
def add_to_cart(request, menu_item_id):
    menu_item = get_object_or_404(MenuItem, id=menu_item_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, menu_item=menu_item)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('view_cart')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('view_cart')
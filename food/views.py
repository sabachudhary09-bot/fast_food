from django.http import HttpResponse
from django.shortcuts import render, redirect
from user_app.models import Product

def index_page(request):
    return render(request, 'index.html')


def offers_page(request):
    return render(request, 'offers.html')
def location_page(request):
    return render(request, 'location.html')


def menu_page(request):
    category = request.GET.get('category')

    if category and category != "all":
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    return render(request, 'menu.html', {'products': products})
from django.shortcuts import render, redirect, get_object_or_404
from user_app.models import Product

# ADD TO CART
def cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        cart = request.session.get("cart", {})

        qty = int(request.POST.get("quantity", 1))
        size = request.POST.get("size")
        order_type = request.POST.get("order_type")
        flavour = request.POST.get("flavour")

        key = str(product_id)

        if key in cart:
            cart[key]["quantity"] += qty
        else:
            cart[key] = {
                "name": product.name,
                "price": float(product.price),
                "quantity": qty,
                "size": size,
                "order_type": order_type,
                "flavour": flavour,
                "image": product.image.url if product.image else ""
            }

        request.session["cart"] = cart

    return redirect('view_cart')


# VIEW CART PAGE
from urllib.parse import quote

def view_cart(request):
    cart = request.session.get("cart", {})
    total = 0

    message = "🛒 *New Order*\n\n"

    for item in cart.values():
        price = float(item.get("price", 0))
        qty = int(item.get("quantity", 0))

        item_total = price * qty
        total += item_total

        message += (
            f"🍔 {item.get('name')}\n"
            f"Size: {item.get('size')}\n"
            f"Flavour: {item.get('flavour')}\n"
            f"Order Type: {item.get('order_type')}\n"
            f"Qty: {qty}\n"
            f"Price: {item_total}\n\n"
        )

    message += f"💰 Total: {total}"

    whatsapp_message = quote(message)

    return render(request, "cart.html", {
        "cart": cart,
        "total": total,
        "whatsapp_message": whatsapp_message
    })


# UPDATE CART
def update_cart(request, product_id, action):
    cart = request.session.get("cart", {})
    key = str(product_id)

    if key in cart:
        if action == "add":
            cart[key]["quantity"] += 1
        elif action == "minus":
            if cart[key]["quantity"] > 1:
                cart[key]["quantity"] -= 1

    request.session["cart"] = cart
    return redirect('view_cart')


# REMOVE ITEM
def remove_from_cart(request, product_id):
    cart = request.session.get("cart", {})

    if str(product_id) in cart:
        del cart[str(product_id)]

    request.session["cart"] = cart
    return redirect('view_cart')
def clear_cart(request):
    request.session["cart"] = {}
    return redirect('view_cart')
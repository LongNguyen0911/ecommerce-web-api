from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt import views
from product.models import Product
from order.models import Order

# Create your views here.
def dashboard(request):
    flag = True
    items = []
    order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':True}
    cartItems = order['get_cart_items']
    if request.user.is_authenticated:
        if not request.user.is_merchant and not request.user.is_superuser:
            customer = request.user
            order, created = Order.objects.get_or_create(customer=customer, completed=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_item
        else:
            flag = False
    #categories = Categorie.objects.all()
    products = Product.objects.filter(approval=True)   
    return render(request, 'store/store.html', {'products': products, 'cartItems': cartItems, 'flag': flag})

def cart(request):
    flag = True
    items = []
    order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':True}
    cartItems = order['get_cart_items']
    if request.user.is_authenticated:
        if not request.user.is_merchant and not request.user.is_superuser:
            customer = request.user
            order, created = Order.objects.get_or_create(customer=customer, completed=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_item
        else:
            flag = False
        #return 'store/login.html'
    return render(request, 'store/cart.html', {'items': items, 'order': order, 'cartItems': cartItems, 'flag': flag})

def checkout(request):
    flag = True
    items = []
    order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':True}
    cartItems = order['get_cart_items']
    if request.user.is_authenticated:
        if not request.user.is_merchant and not request.user.is_superuser:
            customer = request.user
            order, created = Order.objects.get_or_create(customer=customer, completed=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_item
        else:
            flag = False
    return render(request, 'store/checkout.html', {'items': items, 'order': order, 'cartItems': cartItems, 'flag': flag})

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        #content = {'message': 'Hello, World!'}
        return render(request, 'store/store.html')#Response(content)

class CartView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        #content = {'message': 'Hello, World!'}
        return render(request, 'store/cart.html')#Response(content)
    
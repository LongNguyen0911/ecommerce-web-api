from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.views.generic import TemplateView, CreateView
from rest_framework_jwt import views
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.http import JsonResponse
import json
import datetime
from .models import *

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

def category_choosing(request):
    return render(request, 'registration/category_choosing.html')


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def updateItem(request):
    data = json.loads(request.body)
    productId =  data['productId']
    action =  data['action']

    print('productId: ', productId)
    print('action: ', action)

    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, completed=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        if not request.user.is_merchant and not request.user.is_superuser:
            customer = request.user
            order, created = Order.objects.get_or_create(customer=customer, completed=False)
            total = float(data['form']['total'])
            order.transaction_id = transaction_id

            if total == order.get_cart_total:
                order.completed = True
            order.save()

            if order.shipping == True:
                ShippingAddress.objects.create(
                    customer=customer,
                    order=order,
                    address=data['shipping']['address'],
                    city=data['shipping']['city'],
                    state=data['shipping']['state'],
                    zipcode=data['shipping']['zipcode'],
                )
    else:
        print("User is not logged in")
    return JsonResponse('Completed', safe=False)
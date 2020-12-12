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
from .models import *

# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:
        items = []
        order = []
        #cartItems = order[]
    #categories = Categorie.objects.all()
    products = Product.objects.filter(approval=True)   
    return render(request, 'store/store.html', {'products': products, 'cartItems': cartItems})

def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:
        items = []
        order = []
        #return 'store/login.html'
    return render(request, 'store/cart.html', {'items': items, 'order': order, 'cartItems': cartItems})

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:
        items = []
        order = []
    return render(request, 'store/checkout.html', {'items': items, 'order': order, 'cartItems': cartItems})

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
import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from rest_framework import viewsets
from .serializers import ProductSerializer

# Create your views here.
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

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
#    """
#    This viewset automatically provides `list` and `retrieve` actions.
#    """
#    queryset = Categorie.objects.all()
#    serializer_class = UserSerializer
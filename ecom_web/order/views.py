import json
import datetime
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
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
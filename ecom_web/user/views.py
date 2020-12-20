from django.shortcuts import render
from product.models import Categorie
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from rest_framework import viewsets
from .forms import CustomUserCreationForm
from django.views.generic.edit import CreateView
from .models import CustomUser, Business
from .serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('is_merchant', 'is_superuser', 'is_active')

def LogUserIn(request):
    if request.method != "POST":
        return HttpResponse("<script>alert(\"Method Not Allowed\");window.location.replace(\"/\");</script>")
    else:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = authenticate(username=username,password=password)
        login(request, user)

        if user != None:
            return HttpResponse("<script>alert(\"Login Successfully\");window.location.replace(\"/\");</script>")
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect('login/')

def business_info(request):
    if request.method != "POST":
        return HttpResponse("<script>alert(\"Method Not Allowed\");window.location.replace(\"/\");</script>")
    else:
        business = request.user
        business_name = request.POST.get('business_name','')
        business_address = request.POST.get('business_address','')
        zipcode = request.POST.get('business_zipcode','')
        category = request.POST.get('category','')
        c_list = Categorie.objects.all()
        for item in c_list:
            if str(item) == category:
                var_category = item
        
        business_var = Business.objects.create(business=business,business_name=business_name,business_address=business_address,zipcode=zipcode,category=var_category)
        business_var.save()

        if business_var != None:
            return HttpResponse("<script>alert(\"Add Business Infor Successfully\");window.location.replace(\"/\");</script>")
        else:
            messages.error(request, "Error, Try Again")
            return HttpResponseRedirect('/')
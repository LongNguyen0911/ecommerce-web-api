from django.shortcuts import render
from product.models import Categorie
from django.urls import reverse_lazy
from rest_framework import viewsets
from .forms import CustomUserCreationForm
from django.views.generic.edit import CreateView
from .models import CustomUser
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
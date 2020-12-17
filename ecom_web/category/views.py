from django.shortcuts import render
from .models import Categorie
from rest_framework import viewsets
from .serializers import CategorySerializer
from user.forms import BusinessRegisterForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
def category_choosing(request):
    category_list = Categorie.objects.all()
    return render(request, 'registration/category_choosing.html', {'category_list': category_list})

class CategoryChoosingView(CreateView):
    form_class = BusinessRegisterForm
    success_url = reverse_lazy('dashboard')
    template_name = 'registration/category_choosing.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #user = self.request.user
        context["category_list"] = Categorie.objects.all()
        return context

class CategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Categorie.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('cat_id', 'cat_name')
from django.urls import path
from . import views

urlpatterns = [
    path('process_order/', views.processOrder, name='process_order'),
]
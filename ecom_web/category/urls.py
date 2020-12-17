from django.urls import path
from category import views

urlpatterns = [
    path('category_choosing/', views.CategoryChoosingView.as_view(), name='category_choosing'),
    path('categories/', views.CategoryViewSet.as_view({'get': 'list'}), name='category_list'),
    path('categories/<int:pk>/', views.CategoryViewSet.as_view({'get': 'retrieve'}), name='category_detail'),
]
from django.urls import path
from category import views
from user.views import business_info

urlpatterns = [
    path('category_choosing/', views.CategoryChoosingView.as_view(), name='category_choosing'),
    path('business_info/', business_info, name='business_info'),
    path('categories/', views.CategoryViewSet.as_view({'get': 'list'}), name='category_list'),
    path('categories/<int:pk>/', views.CategoryViewSet.as_view({'get': 'retrieve'}), name='category_detail'),
]
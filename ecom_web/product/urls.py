from django.urls import path
from product import views

urlpatterns = [
    path('update_item/', views.updateItem, name='update_item'),
    path('products/', views.ProductViewSet.as_view({'get': 'list'}), name='product_list'),
    path('products/<int:pk>/', views.ProductViewSet.as_view({'get': 'retrieve'}), name='product_detail'),
]
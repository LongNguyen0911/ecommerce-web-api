from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('hello/', views.HelloView.as_view(), name='hello'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
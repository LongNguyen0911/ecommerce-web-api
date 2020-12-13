from django.urls import path, include
from . import views
from rest_framework_simplejwt import views as jwt_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('category_choosing/', views.category_choosing, name='category_choosing'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
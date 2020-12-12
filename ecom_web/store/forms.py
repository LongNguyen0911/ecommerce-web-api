from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import *

CAT_CHOOSING = []

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'is_merchant')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email',)

class BusinessRegisterForm(UserCreationForm):   
    objects = Categorie.objects.all()
    for i in objects:
        CAT_CHOOSING.append(str(i))
    class Meta:
        model = Merchant
        fields = ('business_owner_name', 'business_name', 'business_address', 'zipcode')
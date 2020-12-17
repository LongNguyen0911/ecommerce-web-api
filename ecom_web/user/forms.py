from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import *

CAT_CHOOSING = []

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'is_merchant', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email',)

class BusinessRegisterForm(ModelForm):   
#    objects = Categorie.objects.all()
#    for i in objects:
#        CAT_CHOOSING.append(str(i))
    class Meta:
        model = Business
        fields = ('__all__')
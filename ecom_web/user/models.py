from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from category.models import Categorie

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    is_merchant = models.BooleanField(_('merchant signup'), default=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

class Business(models.Model):
    business = models.OneToOneField(CustomUser, on_delete=models.CASCADE, limit_choices_to={'is_merchant': True},)
    business_name = models.CharField(max_length=200, blank=True)
    business_address = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=200, blank=True)
    category = models.OneToOneField(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.business_name

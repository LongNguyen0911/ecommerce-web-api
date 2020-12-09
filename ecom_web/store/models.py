from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    is_merchant = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'is_merchant': True},)
    product_name = models.CharField(max_length=200)
    produtc_des = models.TextField()
    price = models.FloatField(default=0.0)
    approval = models.BooleanField(default=False)
    def __str__(self):
        return self.product_id

class Categorie(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=200)
    description = models.TextField()
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return self.cat_name

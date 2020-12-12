from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    is_merchant = models.BooleanField(_('merchant signup'), default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Customer(models.Model):
    customer = models.OneToOneField(CustomUser, on_delete=models.CASCADE, limit_choices_to={'is_merchant': False, 'is_superuser': False},)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Merchant(models.Model):
    customer = models.OneToOneField(CustomUser, on_delete=models.CASCADE, limit_choices_to={'is_merchant': True},)
    name = models.CharField(max_length=200, blank=True)
    business_owner_name = models.CharField(max_length=200)
    business_name = models.CharField(max_length=200, blank=True)
    business_address = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=200, blank=True)
    categories_list = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Categorie(models.Model):
    #cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=200)
    description = models.TextField()
    #merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, )
    def __str__(self):
        return self.cat_name

class Product(models.Model):
    #product_id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    #produtc_des = models.TextField()
    price = models.FloatField(default=0.0)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    approval = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.product_name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'is_merchant': False, 'is_superuser': False},)
    date_ordered = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200)
    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_item(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'is_merchant': False, 'is_superuser': False},)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
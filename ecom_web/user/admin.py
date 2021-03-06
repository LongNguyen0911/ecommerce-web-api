from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *
from product.models import *
from order.models import *
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'is_merchant', 'is_active', 'first_name', 'last_name')
    list_filter = ('username', 'email', 'is_merchant', 'is_active', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_merchant', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_merchant', 'is_active')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Business)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Product)
admin.site.register(Categorie)
admin.site.unregister(Group)
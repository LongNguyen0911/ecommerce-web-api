from django.db import models
from user.models import Business
from category.models import Categorie
# Create your models here.

class Product(models.Model):
    owner = models.ForeignKey(Business, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    price = models.FloatField(default=0.0)
    category = models.OneToOneField(Categorie, on_delete=models.CASCADE)
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
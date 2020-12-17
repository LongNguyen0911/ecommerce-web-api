from django.db import models
from user.models import Business

# Create your models here.
class Categorie(models.Model):
    #cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=200)
    description = models.TextField()
    #merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, )
    def __str__(self):
        return self.cat_name

class Product(models.Model):
    #product_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Business, on_delete=models.CASCADE)
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
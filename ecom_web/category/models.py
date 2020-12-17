from django.db import models

# Create your models here.
class Categorie(models.Model):
    cat_id = models.IntegerField(blank=True, null=True)
    cat_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.cat_name
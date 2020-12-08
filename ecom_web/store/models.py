from django.db import models
import requests
# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.TextField()
    is_merchant = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    token = models.CharField(max_length=350)

    def __str__(self):
        return self.username

class Merchant(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.TextField()
    is_merchant = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    token = models.CharField(max_length=350)

    def __str__(self):
        return self.username

def encrypt_pwd(username, password):
    link = "http://localhost:8000/api/token/"
    payload = {'username': username, 'password': password}
    token = requests.post(link, data = payload).json()
    access_token = token['access']
    refresh_token = token['refresh']
    return (access_token, refresh_token)
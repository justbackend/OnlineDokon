from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    ism = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    jins = models.CharField(max_length=10)
    manzil = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)

    def __str__(self):
        return self.username


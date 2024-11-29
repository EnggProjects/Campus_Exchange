from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    college = models.ForeignKey('College', null=True, blank=True, on_delete=models.SET_NULL)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

    @property
    def products_count(self):
        return self.product_set.count()

class College(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)

    def __str__(self):
        return self.name
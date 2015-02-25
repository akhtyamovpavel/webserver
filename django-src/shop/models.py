from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Seller(models.Model):
    user = models.OneToOneField(User)
    money = models.IntegerField()

    def __str__(self):
        return self.user.username


class Good(models.Model):
    name = models.TextField()
    content = models.TextField()
    price = models.IntegerField()
    seller = models.ForeignKey(Seller)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User)
    money = models.IntegerField()

    def __str__(self):
        return self.user.username
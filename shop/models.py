import datetime

from django.db import models

# Create your models here.
from accounts.models import User


class Smartphone(models.Model):
    brand_name = models.CharField(max_length=20)
    model_name = models.CharField(max_length=20)
    price = models.FloatField(max_length=10)
    serial_number = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    memory = models.CharField(max_length=20)

    smartphone_img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.brand_name + " " + self.model_name


class Purchase(models.Model):
    username = models.ForeignKey(User, related_name='user_id', on_delete=models.CASCADE)
    serial_number = models.ForeignKey(Smartphone, related_name='serial_number_id', on_delete=models.CASCADE)

    def __str__(self):
        return self.username.first_name + " " + self.serial_number.brand_name


class Claim(models.Model):
    owner = models.ForeignKey(Purchase, related_name='ownership', on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='date_created', auto_now_add=True)
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=500)
    theft = models.CharField(max_length=3, default='no')
    is_accepted = models.BooleanField(default=False)
    is_repairable = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)


    def __str__(self):
        return self.owner.username.first_name + " " + self.subject


class Laptop(models.Model):
    brand_name = models.CharField(max_length=20)
    model_name = models.CharField(max_length=20)
    price = models.FloatField(max_length=10)
    serial_number = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    memory = models.CharField(max_length=20)
    ram = models.CharField(max_length=10)

    laptop_img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.brand_name + " " + self.model_name


class Automobile(models.Model):
    manufacturer = models.CharField(max_length=20)
    model_name = models.CharField(max_length=20)
    price = models.FloatField(max_length=10)
    serial_number = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    mileage = models.CharField(max_length=20)

    automobile_img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.manufacturer + " " + self.model_name


class PurchaseLaptop(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    serial_number = models.ForeignKey(Laptop, on_delete=models.CASCADE)

    def __str__(self):
        return self.username.first_name + " " + self.serial_number.brand_name


class ClaimLaptop(models.Model):
    owner = models.ForeignKey(PurchaseLaptop, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='date_created', auto_now_add=True)
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=500)
    theft = models.CharField(max_length=3, default='no')
    is_accepted = models.BooleanField(default=False)
    is_repairable = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)

    def __str__(self):
        return self.owner.username.first_name + " " + self.subject


class PurchaseAutomobile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    serial_number = models.ForeignKey(Automobile, on_delete=models.CASCADE)

    def __str__(self):
        return self.username.first_name + " " + self.serial_number.manufacturer


class ClaimAutomobile(models.Model):
    owner = models.ForeignKey(PurchaseAutomobile, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='date_created', auto_now_add=True)
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=500)
    theft = models.CharField(max_length=3, default='no')
    is_accepted = models.BooleanField(default=False)
    is_repairable = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)

    def __str__(self):
        return self.owner.username.first_name + " " + self.subject

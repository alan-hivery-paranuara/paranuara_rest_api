from django.db import models


class FoodItem(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    category = models.CharField(max_length=128, choices=(('vegetable', 'Vegetable'), ('fruit', 'Fruit')))


class Company(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)


class Person(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, related_name='employees')
    age = models.IntegerField(default=0, blank=True, null=True)
    deceased = models.BooleanField(default=False)
    eye_color = models.CharField(max_length=128, blank=True, null=True)
    email = models.CharField(max_length=256, blank=True, null=True)
    phone = models.CharField(max_length=128, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    favourite_foods = models.ManyToManyField(FoodItem, blank=True)
    friends = models.ManyToManyField('Person', blank=True)


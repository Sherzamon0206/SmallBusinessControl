from django.db import models
from django.contrib.auth.models import User

from django.template.defaultfilters import slugify
class Tadbirkor(models.Model):
    user = models.ForeignKey(User, models.CASCADE, null=True, blank=True)
    phone_number = models.CharField(max_length=25, null=True, blank=True)
    company_name = models.CharField(max_length=125,null=True, blank=True)
    logo = models.ImageField(upload_to='images', null=True,blank=True)
    address = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username}"



class Invoice(models.Model):
    billto = models.CharField(max_length=225, null=True, blank=True)
    shipto = models.CharField(max_length=225, null=True, blank=True)
    created_date = models.DateField(blank=True, null=True)
    due_days = models.IntegerField(null=True, blank=True)
    name = models.CharField(blank=True, null=True, max_length=125)
    tax_rate = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name


class Invoice_product(models.Model):
    invoice = models.ForeignKey(Invoice, models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=255,null=True, blank=True)
    unit_price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} product to {self.invoice.name}"


class Free_advice(models.Model):
    title = models.CharField(max_length=125, null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='images')
    description = models.TextField(blank=True, null=True)
    number_of_view = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, max_length=125)
    created_date = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class WhatWillDo(models.Model):
    question = models.CharField(max_length=255, null=True, blank=True)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.question


class Homethemes(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.title


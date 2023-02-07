from django.db import models


# Create your models here.
class Items(models.Model):
    objects = models.Manager()

    item_name = models.CharField(max_length=500)
    category_name = models.CharField(max_length=500)
    quantity = models.IntegerField()
    date = models.DateField(verbose_name='Date')


class Category(models.Model):
    objects = models.Manager()

    categoryName = models.OneToOneField(Items, on_delete=models.CASCADE, max_length=500, primary_key=True)
    category_date = models.DateField(verbose_name='Category Date')

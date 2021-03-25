from django.db import models
from django import forms

# Create your models here.
class User(models.Model):
    alias = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=40, null=False, )
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(primary_key=True, unique=True)
    password = models.CharField(max_length=30)
    birth_date = models.DateField()
    GENDER = [
        ("H","Hombre"),
        ("M","Mujer"),
    ]
    gender = models.CharField(max_length=1, choices = GENDER)
    city = models.CharField(max_length=50)

    def __str__(self):
        return "{} {} {}".format(self.alias, self.email, self.birth_date)

class Store(models.Model):
    id_store = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    url = models.URLField()
    number_products = models.PositiveIntegerField()

    def __str__(self):
        return "{} {} {}".format(self.id_store, self.name, self.url)

class Category(models.Model):
    NAME = [
        ("L6","Labial"),
        ("S7","Sombras"),
        ("R5","Rubor"),
        ("B5","Bases"),
        ("D0","Delineador"),
        ("I0","Iluminador"),
        ("C9","Corrector")
    ]
    name = models.CharField(choices=NAME, max_length=2)

    def __str__(self):
        return "{}".format(self.name)

class Product_Store(models.Model):
    id_product = models.AutoField(primary_key=True)
    name_product = models.CharField(max_length=50)
    mark = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length= 256)
    image = models.CharField(max_length=256)
    id_store = models.ForeignKey(Store,related_name="store_id", on_delete=models.CASCADE)
    name_category = models.ForeignKey(Category, related_name="category_name", on_delete=models.CASCADE)

    def __str__(self):
        return "{}{}{}".format(self.id_product, self.name_product, self.price)

class Product(models.Model):
    name_product = models.CharField(max_length=50)
    mark = models.CharField(max_length=30)
    image = models.CharField(max_length=256)
    name_category = models.ForeignKey(Category, related_name="product_category", on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product_Store, related_name="store_product", on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.id_product, self.name_product, self.mark)

class Wish_list(models.Model):
    email_list = models.ForeignKey(User, related_name="user_email", on_delete= models.CASCADE)
    id_product = models.ForeignKey(Product_Store, related_name="product_id", on_delete=models.CASCADE)

    def __str__(self):
        return "{}{}".format(self.email_list, self.id_product)

from django.db import models
from account.models import Person, Address


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    imageUrl = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)


class Cart(models.Model):
    cartSession = models.CharField(max_length=200)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=10,decimal_places=2)
    productPrice = models.DecimalField(max_digits=10,decimal_places=2)


class Transaction(models.Model):
    ref = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    paymentMethod = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING)


class Order(models.Model):
    shippingAddress = models.ForeignKey(Address, on_delete=models.DO_NOTHING,related_name="shipping_address")
    billingAddress = models.ForeignKey(Address, on_delete=models.DO_NOTHING,related_name="billing_address")
    transaction = models.ForeignKey(Transaction, on_delete=models.DO_NOTHING)
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=200)

from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=15)
    email=models.CharField(max_length=200)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY=(
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor')
    )
    name=models.CharField(max_length=200)
    price=models.FloatField(max_length=200)
    category=models.CharField(max_length=200,choices=CATEGORY)
    description=models.CharField(max_length=200)
    date_created=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name
class Order(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('Out of delivery','Out of delivery'),
        ('Delivered','Delivered')
        
    )
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=200,choices=STATUS)
    def __str__(self):
        return self.product.name


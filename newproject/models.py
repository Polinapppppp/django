from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,  decimal_places=2)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
from django.db import models


# Create your models here.


class Stock(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20, unique=True)
    cost = models.IntegerField()
    price = models.IntegerField()
    number_available = models.IntegerField()
    initial_quantity = models.IntegerField()


    def __str__(self):
        return f"{self.name}"


class Receipt(models.Model):
    customer_name = models.CharField(max_length=30)
    item = models.ForeignKey(Stock, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    amount_in_words = models.CharField(max_length=100)
    balance = models.IntegerField()

    def __str__(self):
        return f"Customer Name: {self.customer_name} Receipt: {self.id}"



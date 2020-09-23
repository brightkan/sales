from django.db import models


# Create your models here.


class Location(models.Model):
    country = models.CharField(max_length=20)
    region = models.CharField(max_length=20)

    def __str__(self):
        return "{} - {}".format(self.country, self.region)


class Item(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type


class Order(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order_id = models.IntegerField(unique=True)
    priority = models.CharField(max_length=1)
    date = models.DateField()
    ship_date = models.DateField()
    units_sold = models.IntegerField()
    unit_cost = models.IntegerField()
    unit_price = models.IntegerField()

    @property
    def total_cost(self):
        total_cost = self.unit_cost * self.units_sold
        return total_cost

    @property
    def total_revenue(self):
        total_revenue = self.units_sold * self.unit_price
        return total_revenue

    @property
    def total_profit(self):
        total_profit = self.total_revenue - self.total_cost
        return total_profit

    def __str__(self):
        return self.order_id


class CSV(models.Model):
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File ID: {self.id}"

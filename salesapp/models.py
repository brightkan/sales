from django.db import models


# Create your models here.


class Location(models.Model):
    country = models.CharField(max_length=20)
    region = models.CharField(max_length=20)

    class Meta:
        unique_together = ("country", "region")

    def __str__(self):
        return "{} - {}".format(self.country, self.region)


class Item(models.Model):
    type = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.type}"


class Order(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    sales_channel = models.CharField(max_length=20, blank=True)
    order_id = models.IntegerField(unique=True)
    priority = models.CharField(max_length=1)
    date = models.DateField()
    ship_date = models.DateField()
    units_sold = models.IntegerField()
    unit_cost = models.FloatField()
    unit_price = models.FloatField()

    @property
    def total_cost(self):
        total_cost = self.unit_cost * self.units_sold
        return round(total_cost, 2)

    @property
    def total_revenue(self):
        total_revenue = self.units_sold * self.unit_price
        return round(total_revenue, 2)

    @property
    def total_profit(self):
        total_profit = self.total_revenue - self.total_cost
        return round(total_profit, 2)

    def __str__(self):
        return f"Order - {self.order_id}"


class CSV(models.Model):
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File ID: {self.id}"

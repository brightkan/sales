from django.db import models
from django.db.models import Sum
from django.utils import timezone


class TrackSetting(models.Model):
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(TrackSetting, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Item(models.Model):
    name = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=20)
    cost = models.IntegerField()
    price = models.IntegerField()
    number_in_stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"

    @property
    def total_quantity_sold(self):
        track_setting = TrackSetting.load()
        start_date_str = track_setting.start_date.isoformat()
        end_date_str = track_setting.end_date.isoformat()
        receipts = Receipt.objects.filter(item=self, date__range=[start_date_str, end_date_str])
        sum = receipts.aggregate(Sum('quantity'))
        quantity = sum['quantity__sum']
        if quantity is None:
            return 0
        return quantity

    @property
    def total_amount_sold(self):
        return self.price * self.total_quantity_sold

    @property
    def total_cost(self):
        return self.cost * self.total_quantity_sold

    @property
    def total_profit(self):
        return self.total_amount_sold - self.total_cost


    @property
    def total_quantity_stocked(self):
        track_setting = TrackSetting.load()
        start_date_str = track_setting.start_date.isoformat()
        end_date_str = track_setting.end_date.isoformat()
        item_stockings = ItemStocking.objects.filter(item=self, date__range=[start_date_str, end_date_str])
        sum = item_stockings.aggregate(Sum('quantity'))
        quantity = sum['quantity__sum']
        if quantity is None:
            return 0
        return quantity

    @property
    def demand_percentage(self):
        try:
            demand_percentage = ((self.total_quantity_sold / self.total_quantity_stocked) * 100)
        except ZeroDivisionError:
            return 0
        return int(demand_percentage)

    @property
    def demand_percentage_str(self):
        if self.demand_percentage < 30 or self.demand_percentage == 0:
            return "Item not moving"
        elif 30 < self.demand_percentage < 60:
            return "Average Demand"
        else:
            return "Moving Fast"


class Receipt(models.Model):
    CASH_OR_CHEQUE = [
        ("Cash", "Cash"),
        ("Cheque", "Cheque")
    ]

    date = models.DateField()
    customer_name = models.CharField(max_length=30)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    amount_in_words = models.CharField(max_length=100)
    cash_or_cheque = models.CharField(max_length=7, choices=CASH_OR_CHEQUE)
    balance = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.item.number_in_stock > 0:
            # Reduce stock available
            item = self.item
            item.number_in_stock = item.number_in_stock - self.quantity
            item.save()
        super(Receipt, self).save(*args, **kwargs)

    def __str__(self):
        return f"Customer Name: {self.customer_name} Receipt: {self.id}"

    @property
    def profit(self):
        return self.total_price - self.total_cost

    @property
    def total_price(self):
        return self.item.price * self.quantity

    @property
    def total_cost(self):
        return self.item.cost * self.quantity


class ItemStocking(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.IntegerField()

    def save(self, *args, **kwargs):
        # Increase stock available
        item = self.item
        item.number_in_stock = item.number_in_stock + self.quantity
        item.save()
        super(ItemStocking, self).save(*args, **kwargs)

    def __str__(self):
        return f"Item Stocking: {self.id}"

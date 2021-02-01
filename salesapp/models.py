from django.db import models
from django.utils import timezone


class Item(models.Model):
    name = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=20)
    cost = models.IntegerField()
    price = models.IntegerField()
    number_in_stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


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

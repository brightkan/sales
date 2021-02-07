from django.db.models import Sum

from salesapp.models import Receipt, Item, TrackSetting, ItemStocking


def get_receipt(id):
    return Receipt.objects.get(pk=id)


def get_item(id):
    return Item.objects.get(pk=id)


def get_track_setting():
    return TrackSetting.load()


def get_all_items():
    return Item.objects.all()


def get_all_item_stockings():
    return ItemStocking.objects.all()


def get_item_stocking(id):
    return ItemStocking.objects.get(pk=id)


def get_quantity(items) -> int:
    sum = items.aggregate(Sum('quantity'))
    quantity = sum['quantity__sum']
    return quantity


def get_item_stockings(item, start_date, end_date):
    item_stockings = ItemStocking.objects.filter(item=item, date__range=[start_date, end_date])
    return item_stockings


def get_receipts(item, start_date, end_date):
    receipts = Receipt.objects.filter(item=item, date__range=[start_date, end_date])
    return receipts

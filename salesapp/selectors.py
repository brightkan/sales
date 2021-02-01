from salesapp.models import Receipt, Item, TrackSetting


def get_receipt(id):
    return Receipt.objects.get(pk=id)


def get_item(id):
    return Item.objects.get(pk=id)


def get_track_setting():
    return TrackSetting.load()


def get_all_items():
    return Item.objects.all()

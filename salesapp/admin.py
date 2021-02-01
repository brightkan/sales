from django.contrib import admin

# Register your models here.
from salesapp.models import Item, Receipt, ItemStocking, TrackSetting

admin.site.register(Item)
admin.site.register(Receipt)
admin.site.register(ItemStocking)
admin.site.register(TrackSetting)

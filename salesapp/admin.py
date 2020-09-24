from django.contrib import admin

# Register your models here.
from salesapp.models import CSV, Location, Item, Order

admin.site.register(CSV)
admin.site.register(Location)
admin.site.register(Item)
admin.site.register(Order)
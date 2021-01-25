from django.contrib import admin

# Register your models here.
from salesapp.models import Stock, Receipt


admin.site.register(Stock)
admin.site.register(Receipt)
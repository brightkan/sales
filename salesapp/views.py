from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.urls import reverse

from salesapp.calculations import get_total_profit
from salesapp.forms import CSVModelForm
from salesapp.models import CSV, Order
from salesapp.services import create_item_and_location_objects, create_order_objects


def dashboard_page(request):
    context = {
        "dashboard": "active",
    }
    return render(request, "dashboard.html", context)


def sales_report_page(request):
    if request.POST:
        iso_date_string1 = request.POST.get("start_date")
        iso_date_string2 = request.POST.get("end_date")
        orders = Order.objects.filter(date__range=[iso_date_string1, iso_date_string2])
        total_profit = get_total_profit(orders)
        context = {
            "dashboard": "active",
            "orders": orders,
            "start_date": iso_date_string1,
            "end_date": iso_date_string2,
            "total_profit":  "%0.2f" % total_profit
        }
        return render(request, "sales_report.html", context)
    else:
        return HttpResponseRedirect(reverse(dashboard_page))


def manage_sales_records_page(request):
    form = CSVModelForm()
    if request.POST:
        form = CSVModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            csv_obj = CSV.objects.get(activated=False)
            csv_obj.activated = True
            csv_obj.save()
            create_item_and_location_objects(csv_obj)
            create_order_objects(csv_obj)
            csv_obj.delete()
            messages.warning(request, "File uploaded successfully")
            return HttpResponseRedirect(reverse(manage_sales_records_page))
        else:
            messages.warning(request, "Form is not valid")

    context = {
        "manage_sales_records": "active",
        "form": form,
    }
    return render(request, "sales_records.html", context)

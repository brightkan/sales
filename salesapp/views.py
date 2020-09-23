import csv

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from salesapp.forms import CSVModelForm
from salesapp.models import CSV


def dashboard_page(request):
    context = {
        "dashboard": "active"
    }
    return render(request, "dashboard.html", context)


def manage_sales_records_page(request):
    form = CSVModelForm()
    if request.POST:
        form = CSVModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            csv_obj = CSV.objects.get(activated=False)
            with open(csv_obj.file_name.path, 'r') as f:
                reader = csv.reader(f)

                for i, row in enumerate(reader):
                    if i == 0:
                        pass
                    else:
                        print(row)

            messages.warning(request, "File uploaded successfully")
            return HttpResponseRedirect(reverse(manage_sales_records_page))
        else:
            messages.warning(request, "Form is not valid")

    context = {
        "manage_sales_records": "active",
        "form": form
    }
    return render(request, "sales_records.html", context)

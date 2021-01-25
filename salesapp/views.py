from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from num2words import num2words

from salesapp.calculations import get_total_profit
from salesapp.forms import ReceiptForm
from salesapp.models import Receipt
from salesapp.services import get_item


def login_page(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse(report_page))
            # Redirect to a success page.
        else:
            if user is not None:
                return HttpResponseRedirect(reverse(report_page))
            messages.warning(request, "Invalid Credentials")
            return HttpResponseRedirect(reverse(login_page))
            # Return an 'invalid login' error message.
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse(login_page))


@login_required(login_url="/")
def report_page(request):
    context = {
        "report": "active",
    }
    return render(request, "report.html", context)


@login_required(login_url="/")
def sales_report_page(request):
    if request.POST:
        iso_date_string1 = request.POST.get("start_date")
        iso_date_string2 = request.POST.get("end_date")
        orders = Order.objects.filter(date__range=[iso_date_string1, iso_date_string2])
        total_profit = get_total_profit(orders)
        context = {
            "report": "active",
            "orders": orders,
            "start_date": iso_date_string1,
            "end_date": iso_date_string2,
            "total_profit": "%0.2f" % total_profit
        }
        return render(request, "sales_report.html", context)
    else:
        return HttpResponseRedirect(reverse(report_page))


def manage_receipts_page(request):
    form = ReceiptForm()
    if request.POST:
        form = ReceiptForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(manage_receipts_page))
        else:
            messages.warning(request, "Form is not valid")

    receipts = Receipt.objects.all()
    context = {
        "manage_receipts": "active",
        "receipts": receipts,
        "form": form,
    }
    return render(request, "manage_receipts.html", context)


def convert_amount_to_words(request):
    amount = request.GET['amount']
    amount_in_words = num2words(amount).capitalize()
    return JsonResponse({'success': True, 'amount_in_words': amount_in_words})


def get_balance(request):
    item_id = request.GET["item_id"]
    item = get_item(item_id)
    amount = request.GET["amount"]
    print("The amount is", amount)
    print("The Item price is", item.price)
    balance = int(amount) - item.price
    return JsonResponse({'success': True, 'balance': balance})

from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from num2words import num2words

from salesapp.forms import ReceiptForm
from salesapp.models import Receipt
from salesapp.procedures import render_to_pdf
from salesapp.selectors import get_receipt
from salesapp.services import get_item


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


def edit_receipt_page(request, receipt_id):
    receipt = get_receipt(receipt_id)
    form = ReceiptForm(instance=receipt)
    if request.method == "POST":
        form = ReceiptForm(request.POST, request.FILES, instance=receipt)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully edited a recipt")
        else:
            messages.error(request, "Integrity problems while saving receipt")
        return HttpResponseRedirect(reverse(manage_receipts_page))
    context = {
        "receipt": "active",
        "form": form,
    }
    return render(request, "edit_receipt.html", context)


def delete_receipt(request, receipt_id):
    receipt = get_receipt(receipt_id)
    receipt.delete()
    messages.success(request, "Successfully deleted a receipt")
    return HttpResponseRedirect(reverse(manage_receipts_page))


def convert_amount_to_words(request):
    amount = request.GET['amount']
    amount_in_words = num2words(amount).capitalize()
    return JsonResponse({'success': True, 'amount_in_words': amount_in_words})


def get_balance(request):
    item_id = request.GET["item_id"]
    item = get_item(item_id)
    amount = request.GET["amount"]
    balance = int(amount) - item.price
    return JsonResponse({'success': True, 'balance': balance})


def generate_receipt_pdf(request, receipt_id):
    receipt = get_receipt(receipt_id)
    context = {
        "receipt": receipt
    }
    pdf = render_to_pdf('pdfs/receipt.html', context)
    return HttpResponse(pdf, content_type='application/pdf')

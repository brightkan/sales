from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from salesapp.forms import ItemStockingForm
from salesapp.selectors import get_all_item_stockings, get_item_stocking


def manage_item_stockings_page(request):
    form = ItemStockingForm()
    if request.POST:
        form = ItemStockingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(manage_item_stockings_page))
        else:
            messages.warning(request, "Form is not valid")

    item_stockings = get_all_item_stockings()
    context = {
        "manage_item_stockings": "active",
        "item_stockings": item_stockings,
        "form": form,
    }
    return render(request, "item_stockings/manage_item_stockings.html", context)


def edit_item_stocking_page(request, item_stocking_id):
    item_stocking = get_item_stocking(item_stocking_id)
    form = ItemStockingForm(instance=item_stocking)
    if request.method == "POST":
        form = ItemStockingForm(request.POST, request.FILES, instance=item_stocking)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully edited a item stocking")
        else:
            messages.error(request, "Integrity problems while saving stock")
        return HttpResponseRedirect(reverse(manage_item_stockings_page))
    context = {
        "manage_item_stockings": "active",
        "form": form,
    }
    return render(request, "item_stockings/edit_item_stocking.html", context)


def delete_item_stocking(request, item_stocking_id):
    item_stocking = get_item_stocking(item_stocking_id)
    item_stocking.delete()
    messages.success(request, "Successfully deleted a item stocking")
    return HttpResponseRedirect(reverse(manage_item_stockings_page))






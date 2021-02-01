from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from salesapp.forms import ItemForm, TrackSettingForm
from salesapp.selectors import get_item, get_track_setting, get_all_items


def manage_items_page(request):
    form = ItemForm()
    if request.POST:
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(manage_items_page))
        else:
            messages.warning(request, "Form is not valid")

    items = get_all_items()
    track_setting = get_track_setting()
    track_settings_form = TrackSettingForm(instance=track_setting)
    context = {
        "manage_items": "active",
        "items": items,
        "form": form,
        "track_settings_form": track_settings_form,
    }
    return render(request, "items/manage_items.html", context)


def edit_track_setting(request):
    track_setting = get_track_setting()
    if request.method == "POST":
        form = TrackSettingForm(request.POST, request.FILES, instance=track_setting)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully edited track settings")
        else:
            messages.error(request, "Integrity problems while editing track settings")
        return HttpResponseRedirect(reverse(manage_items_page))
    return HttpResponseRedirect(reverse(manage_items_page))


def edit_item_page(request, item_id):
    item = get_item(item_id)
    form = ItemForm(instance=item)
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully edited a item")
        else:
            messages.error(request, "Integrity problems while saving item")
        return HttpResponseRedirect(reverse(manage_items_page))
    context = {
        "manage_items": "active",
        "form": form,
    }
    return render(request, "items/edit_item.html", context)


def delete_item(request, item_id):
    item = get_item(item_id)
    item.delete()
    messages.success(request, "Successfully deleted a item")
    return HttpResponseRedirect(reverse(manage_items_page))


from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from salesapp.forms import TrackSettingForm
from salesapp.procedures import render_to_pdf
from salesapp.selectors import get_track_setting, get_all_items


def report_page(request):
    track_setting = get_track_setting()
    form = TrackSettingForm(instance=track_setting)
    if request.method == "POST":
        form = TrackSettingForm(request.POST, request.FILES, instance=track_setting)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully edited track settings")
        else:
            messages.error(request, "Integrity problems while editing track settings")

        return HttpResponseRedirect(reverse(report_page))
    items = get_all_items()
    context = {
        "form": form,
        "items": items
    }
    return render(request, "report/report.html", context)


def generate_report_pdf(request):
    items = get_all_items()
    date_range = get_track_setting()
    context = {
         "items": items,
         "date_range": date_range
    }
    pdf = render_to_pdf('pdfs/report.html', context)
    return HttpResponse(pdf, content_type='application/pdf')

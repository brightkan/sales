from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from salesapp.views.receipt_views import manage_receipts_page


def login_page(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse(manage_receipts_page))
            # Redirect to a success page.
        else:
            if user is not None:
                return HttpResponseRedirect(reverse(manage_receipts_page))
            messages.warning(request, "Invalid Credentials")
            return HttpResponseRedirect(reverse(login_page))
            # Return an 'invalid login' error message.
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse(login_page))
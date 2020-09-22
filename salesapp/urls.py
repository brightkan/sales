from django.urls import path

from salesapp.views import dashboardpage
urlpatterns = [
    path('', dashboardpage, name='index_page'),
]
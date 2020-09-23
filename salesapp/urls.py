from django.urls import path

from salesapp.views import dashboard_page, manage_sales_records_page

urlpatterns = [
    path('', dashboard_page, name='dashboard_page'),
    path('manage_sales_records/', manage_sales_records_page, name="manage_sales_records")
]
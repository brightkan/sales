from django.urls import path, reverse

from salesapp.views import report_page, manage_receipts_page, sales_report_page, login_page, logout_view, \
    convert_amount_to_words, get_balance

urlpatterns = [
    path('', login_page, name='login_page'),
    path('manage_receipts/', manage_receipts_page, name="manage_receipts"),
    path('report/', report_page, name='report_page'),
    path('sales_report/', sales_report_page, name="sales_report_page"),
    path('logout/', logout_view, name="logout"),
    path('convert_amount_to_words/', convert_amount_to_words, name="convert_amount_to_words"),
    path('get_balance/', get_balance, name="get_balance")
]


# customJS routes
def javascript_settings():
    js_conf = {
        'convert_amount_to_words': reverse('convert_amount_to_words'),
        'get_balance': reverse('get_balance'),
    }
    return js_conf

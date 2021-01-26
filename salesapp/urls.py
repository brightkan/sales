from django.urls import path, reverse

from salesapp.views.auth_views import login_page, logout_view
from salesapp.views.receipt_views import manage_receipts_page, convert_amount_to_words, get_balance, \
    generate_receipt_pdf, edit_receipt_page, delete_receipt

urlpatterns = [
    path('', login_page, name='login_page'),
    path('manage_receipts/', manage_receipts_page, name="manage_receipts"),
    path('logout/', logout_view, name="logout"),
    path('convert_amount_to_words/', convert_amount_to_words, name="convert_amount_to_words"),
    path('get_balance/', get_balance, name="get_balance"),
    path('generate_receipt_pdf/<int:receipt_id>/', generate_receipt_pdf, name="generate_receipt_pdf"),
    path('edit_receipt_page/<int:receipt_id>/', edit_receipt_page, name="edit_receipt_page"),
    path('delete_receipt/<int:receipt_id>/', delete_receipt, name="delete_receipt")
]


# customJS routes
def javascript_settings():
    js_conf = {
        'convert_amount_to_words': reverse('convert_amount_to_words'),
        'get_balance': reverse('get_balance'),
    }
    return js_conf

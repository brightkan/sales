from django.urls import path, reverse

from salesapp.views.auth_views import login_page, logout_view
from salesapp.views.item_views import manage_items_page, edit_item_page, delete_item, edit_track_setting
from salesapp.views.receipt_views import manage_receipts_page, convert_amount_to_words, get_balance, \
    generate_receipt_pdf, edit_receipt_page, delete_receipt, get_number_in_stock
from salesapp.views.report_views import report_page, generate_report_pdf
from salesapp.views.stock_views import manage_item_stockings_page, edit_item_stocking_page, delete_item_stocking

urlpatterns = [
    path('', login_page, name='login_page'),
    path('manage_receipts/', manage_receipts_page, name="manage_receipts"),
    path('logout/', logout_view, name="logout"),
    path('convert_amount_to_words/', convert_amount_to_words, name="convert_amount_to_words"),
    path('get_balance/', get_balance, name="get_balance"),
    path('get_number_in_stock/', get_number_in_stock, name="get_number_in_stock"),
    path('generate_receipt_pdf/<int:receipt_id>/', generate_receipt_pdf, name="generate_receipt_pdf"),
    path('edit_receipt_page/<int:receipt_id>/', edit_receipt_page, name="edit_receipt_page"),
    path('delete_receipt/<int:receipt_id>/', delete_receipt, name="delete_receipt"),
    path('manage_items/', manage_items_page, name="manage_items"),
    path('edit_item_page/<int:item_id>/', edit_item_page, name="edit_item_page"),
    path('delete_item/<int:item_id>/', delete_item, name="delete_item"),
    path('edit_track_setting/', edit_track_setting, name="edit_track_setting"),
    path('manage_item_stockings/', manage_item_stockings_page, name="manage_item_stockings"),
    path('edit_item_stocking/<int:item_stocking_id>/', edit_item_stocking_page, name="edit_item_stocking"),
    path('delete_item_stocking/<int:item_stocking_id>/', delete_item_stocking, name="delete_item_stocking"),
    path('report/', report_page, name="report"),
    path('generate_report_pdf/', generate_report_pdf, name="generate_report_pdf"),
]


# customJS routes
def javascript_settings():
    js_conf = {
        'convert_amount_to_words': reverse('convert_amount_to_words'),
        'get_balance': reverse('get_balance'),
        'get_number_in_stock': reverse('get_number_in_stock'),
    }
    return js_conf

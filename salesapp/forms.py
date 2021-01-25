from django import forms

from salesapp.models import Stock, Receipt


class ItemForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = "__all__"


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = "__all__"

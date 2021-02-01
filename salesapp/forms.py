from crispy_forms.helper import FormHelper
from django import forms

from salesapp.models import Item, Receipt, TrackSetting


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['number_in_stock'].widget.attrs['readonly'] = True
        self.helper = FormHelper()


class TrackSettingForm(forms.ModelForm):
    class Meta:
        model = TrackSetting
        fields = "__all__"

        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"})
        }


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = "__all__"

        widgets = {
            "date": forms.DateInput(attrs={"type": "date"})
        }

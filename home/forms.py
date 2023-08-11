from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('soft_name', 'soft_type', 'soft_time',
                  'soft_amount', 'soft_desc')

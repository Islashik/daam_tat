from django import forms
from backend.apps.orders.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'address',
            'postal_code',
            'mobile',
            'notice'
        ]
        widgets = {
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'notice': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UserEntryForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    middle_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
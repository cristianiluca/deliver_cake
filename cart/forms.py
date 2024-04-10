from django import forms


class InputQuantity(forms.Form):
    cantitate = forms.DecimalField(label='Cantitate (kg)', max_digits=5, decimal_places=1)


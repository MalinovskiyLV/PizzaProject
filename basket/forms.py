from django import forms

PIZZA_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class BasketAddPizzaForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PIZZA_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

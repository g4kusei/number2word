from django import forms


class NumberForm(forms.Form):
    your_number = forms.IntegerField(label='Your number')

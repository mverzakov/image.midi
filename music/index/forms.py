from django import forms


class IndexForm(forms.Form):
    file = forms.FileField()

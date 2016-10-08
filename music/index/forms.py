from django import forms


class IndexForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

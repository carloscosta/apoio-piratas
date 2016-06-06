
from django import forms


class AskForm(forms.Form):
    your_name   = forms.CharField(label='Seu Nome', max_length=200)
    your_email  = forms.CharField(label='Seu Email', max_length=200)
    status      = 'PE'
    comment     = forms.CharField(label='Pergunte', widget=forms.Textarea)

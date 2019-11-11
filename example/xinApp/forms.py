from django import forms

class xinForm(forms.Form):
    name = forms.CharField(label='What\'s your name')
    line2 = forms.CharField(label='line 2', required=False)
    line3 = forms.CharField(label='line 3')


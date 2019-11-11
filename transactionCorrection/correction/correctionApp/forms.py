from django import forms


class CorrectionForm(forms.Form):
    something1 = forms.CharField(label='something_lable', max_length=100)
    something2 = forms.ChoiceField(label='something2_lable', choices=['c1', 'c2', 'c3'])


class AnotherForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()

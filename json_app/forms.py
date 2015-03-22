from django import forms

class form_file(forms.Form):
    file = forms.FileField()
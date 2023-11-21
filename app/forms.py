from django import forms
from .models import Demo

class DemoForm(forms.ModelForm):
    class Meta:
        model = Demo
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','id':'name'}),
            'age':forms.TextInput(attrs={'class':'form-control'})
        }


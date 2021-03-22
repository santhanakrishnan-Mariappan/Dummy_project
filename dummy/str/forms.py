from django import forms
from .models import model_class

class form_class(forms.ModelForm):
    class Meta:
        model = model_class
        fields = ('name', 'mobile', 'email')


from django import forms
from .models import Outer

class OuterForm(forms.ModelForm):
    class Meta:
        model = Outer
        fields = ("name",)

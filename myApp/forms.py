from django import forms
from .models import Outer,Event, Outer2

class OuterForm(forms.ModelForm):
    class Meta:
        model = Outer
        fields = ("name",)
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ("name",)
class OuterForm2(forms.ModelForm):
    class Meta:
        model = Outer2
        fields = ("name","school")
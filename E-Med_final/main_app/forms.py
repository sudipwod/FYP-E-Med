from django import forms
from .models import appointment

class appointmentform(forms.ModelForm):
    class Meta:
        model = appointment
        fields = ["name", "email", "service","time", "note"]
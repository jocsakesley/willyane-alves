
from django import forms
from .models import KitService, Service

class ServiceForm(forms.ModelForm):
    DURATION_CHOICES = [
        ("00:30:00", "00:30"),
        ("01:00:00", "01:00"),
        ("01:30:00", "01:30"),
        ("02:00:00", "02:00"),
        ("02:30:00", "02:30"),
        ("03:00:00", "03:00"),
    ]
    duration = forms.CharField(label='Duração', widget=forms.Select(choices=DURATION_CHOICES))
    class Meta:
        model = Service
        fields = '__all__'

class KitServiceForm(forms.ModelForm):
    class Meta:
        model = KitService
        fields = '__all__'
from django import forms

class ServiceForm(forms.Form):
    DURATION_CHOICES = [
        ("00:30:00", "00:30"),
        ("01:00:00", "01:00"),
        ("01:30:00", "01:30"),
        ("02:00:00", "02:00"),
        ("02:30:00", "02:30"),
        ("03:00:00", "03:00"),
    ]
    service = forms.CharField(label='Serviço')
    price = forms.DecimalField(label='Valor', decimal_places=2)
    duration = forms.DurationField(label='Duração', widget=forms.Select(choices=DURATION_CHOICES))
    cost = forms.DecimalField(label='Custo', decimal_places=2)



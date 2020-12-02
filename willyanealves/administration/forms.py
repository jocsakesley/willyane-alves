from django import forms
from datetime import datetime

class DashForm(forms.Form):
    MONTH = (
        (1, "Janeiro"),
        (2, "Fevereiro"),
        (3, "Março"),
        (4, "Abril"),
        (5, "Maio"),
        (6, "Junho"),
        (7, "Julho"),
        (8, "Agosto"),
        (9, "Setembro"),
        (10, "Outubro"),
        (11, "Novembro"),
        (12, "Dezembro"),
    )
    YEAR = ()
    month = forms.IntegerField(label="Mês", widget=forms.Select(choices=MONTH), initial=datetime.today().month)
    year = forms.IntegerField(label="Ano", widget=forms.Select(choices=zip(range(2018, datetime.today().year + 1), range(2018, datetime.today().year + 1))), initial=datetime.today().year)
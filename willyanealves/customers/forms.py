from django import forms
import datetime
class CustomersForm(forms.Form):
    SEX = [("M", "Masculino"), ("F", "Feminino")]
    CITIES = [("NAT", "Natal"), ("PAR", "Parnamirim"), ("SGA", "São Gonçalo do Amarante"), ("EXT", "Extremoz"), ("CEM", "Ceará-Mirim"),
              ("SJM", "São José de Mipibú"), ("OUT", "Outra")]
    name = forms.CharField(label="Nome")
    last_name = forms.CharField(label="Sobrenome")
    cpf = forms.CharField(label="CPF", required=False)
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Telefone")
    sex = forms.CharField(label="Sexo", widget=forms.Select(choices=SEX))
    address = forms.CharField(label="Endereço", required=False)
    city = forms.CharField(label="Cidade", widget=forms.Select(choices=CITIES))
    district =forms.CharField(label="Bairro", required=False)
    birth = forms.DateField(label="Data de nascimento", required=False)

from django import forms
from .models import Cliente
from django.contrib.auth.models import User
from django.db import models
# from django.forms.fields import DateField



class ClienteForm(forms.ModelForm):

    password = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True, label="Senha")
    confirm_password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput, label="Verifique senha")

    class Meta:
        model = Cliente
        fields = ('username', 'password', 'confirm_password', 'first_name', 'last_name', 'nascimento', 'email', 'profissao', 'estado_civil', 'telefone', 'endereco', 'instagram')
        widgets = {
            'nascimento': forms.DateInput(format="%d/%m/%Y") 
        }

    def clean(self):
        cleaned_data = super(ClienteForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "As senhas inseridas não identicas"
            )

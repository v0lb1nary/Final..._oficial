from django import forms
from .models import Cliente
from django.contrib.auth.models import User
from django.db import models
# from django.forms.fields import DateField



class ClienteForm(forms.ModelForm):
    
    password_ver = forms.CharField(max_length=50, required=True,  label="Verifique senha")
    password = forms.CharField(max_length=50, required=True, label="Senha")

    class Meta:
        model = Cliente
        fields = ('username', 'first_name', 'last_name', 'email', 'telefone', 'nascimento', 'profissao', 'estado_civil')
        widgets = {
            'nascimento': forms.DateInput(format="%d/%m/%Y") 
        }

    def limpar_senha(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_ver']:
            raise forms.ValidationError('As senhas não são iguais!')
        
        else:
            return cd['password']


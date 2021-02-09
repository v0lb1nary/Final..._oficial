from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ClienteForm
from .models import Modalidade

def home_pag(request):
    modalidades = Modalidade.objects.all()
    return render(request, 'Espaco_Tao/home.html', {'modalidade': modalidades})

@login_required
def painel_controle_pag(request):
    user_login = User.objects.all()
    return render(request, 'Espaco_Tao/painel_controle.html', {'user':user_login})

def cadastro_cliente(request):
    if request.method == "POST":
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            new_cliente = formulario.save(commit=False)
            new_cliente.set_password(formulario.cleaned_data['password'])
            new_cliente.save()
            return render(request, 'Espaco_Tao/cadastro_realizado.html', {'form_cdst':formulario})
    else:
        formulario = ClienteForm()
    return render(request, 'Espaco_Tao/cadastrar.html', {'form_cdst':formulario})

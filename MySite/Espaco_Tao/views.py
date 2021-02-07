from django.shortcuts import render

def home_pag(request):
    return render(request, 'Espaco_Tao/home.html')



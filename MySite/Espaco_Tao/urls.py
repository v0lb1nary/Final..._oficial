from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    path("home/", views.home_pag, name="home"),

    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("painel_controle/", views.painel_controle_pag, name="painel_controle"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path("cadastro/", views.cadastro_cliente, name="cadastro")

]

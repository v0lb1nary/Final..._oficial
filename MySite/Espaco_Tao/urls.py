from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    #& Home
    path("home/", views.home_pag, name="home"),


    #& Reazlização do Login
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("painel_controle/", views.painel_controle_pag, name="painel_controle"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),


    #& Cadastramento
    path("cadastro/", views.cadastro_cliente, name="cadastro"),


    #& Alteração de Senha
    path('redefinir_senha/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('redefinir_senha/concluida/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),


    #& Perca de Senha
    #? Recuração de Senha
    #* Parte O1
    path('recuperar_senha/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('recuperar_senha/recuperada', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    
    #? Redefinição
    #* Parte 02
    path('recuperar_senha/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('recuperar_senha/redefinida/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

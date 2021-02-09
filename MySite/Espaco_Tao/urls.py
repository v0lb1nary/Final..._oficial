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
    path('alterar_senha/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('alterar_senha/alterada/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),


    #& Redefinição de Senha
    path('reiniciar_senha/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reiniciar_senha/reiniciada', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reiniciar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reiniciar/reiniciada/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

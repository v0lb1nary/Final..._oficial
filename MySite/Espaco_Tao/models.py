from django.db import models
from django.contrib.auth.models import User


class Infos_Adicionais(models.Model):
    """ Classe Abstrata """

    telefone = models.CharField(max_length=11, blank=False, default=None, help_text='Campo obrigatorio*')
    endereco = models.CharField(max_length=254, blank=True)
    instagram = models.CharField(max_length=50, blank=True, help_text="")
    
    class Meta:
        abstract = True
    

# ------------------------------------------------------ #


class Terapeuta(Infos_Adicionais, User):
    """ Classe especializada (Insfons_Adicionais e User) """ 

    is_staff = True
    hora_entrada = models.TimeField(auto_now=False, auto_now_add=False, help_text='Entrada para o atendimento')
    hora_alm_entrda = models.TimeField(auto_now=False, auto_now_add=False, help_text='Saida para almoço')
    hora_alm_saida = models.TimeField(auto_now=False, auto_now_add=False, help_text='Retorno do horário de almoço')
    hora_saida = models.TimeField(auto_now=False, auto_now_add=False, help_text='Horário de saida')
    
    class Meta:
        verbose_name = 'Terapeuta'
        verbose_name_plural = 'Terapeutas'

    def __str__(self):
        return self.get_full_name()



class Cliente(Infos_Adicionais, User):
    """ Classe especilizada (Insfons_Adicionais e User) """

    PROFISSAO_CHOICE = (('',''), ('desempregado', 'Desempregado'), ('empregado', 'Empregado'))
    ESTADO_CIVIL_COICE = (('',''), ('solteiro(a)','Solteiro(a)'),('casado(a)','Casado(a)'),('divorciado(a)','Divorciado(a)'),('viúvo(a)','Viúvo(a)'))

    nascimento = models.DateField(auto_now=False, auto_now_add=False, blank=False, default='', help_text='Campo obrigatório*')
    profissao = models.CharField(max_length=20, choices=PROFISSAO_CHOICE, default='', blank=True)
    estado_civil = models.CharField(max_length=20, choices=ESTADO_CIVIL_COICE, default='solterio(a)', blank=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.get_full_name()


# ------------------------------------------------------ #


class Modalidade(models.Model):
    """ Classe Modalidade """

    MODALIDADES_TUPLA = [
        ('', ''),
        ('Terapia', 'Terapia'),
        ('Tai Chi Chuan', 'Tai Chi Chuan'), 
        ('Cone Hindu', 'Cone Hindu'),
        ('Barras de Access', 'Barras de Access'),]

    modalidade = models.CharField(max_length=30, choices=MODALIDADES_TUPLA, default=None, unique=True)
    valor = models.FloatField(blank=False, default=None, help_text='Campo obrigatório*')
    tempo_duracao = models.DurationField(blank=False, default=None, help_text='Campo obrigatório*')
    descricao = models.TextField(blank=True, default=None, help_text='Aqui comente sobre o que e/ou como é realiado essa modalidade')

    class Meta:
        verbose_name = 'Modalidade'
        verbose_name_plural = 'Modalidades'

    def __str__(self):
        return self.modalidade

    # def __repr__(self):
    #     return self.modalidades


# ------------------------------------------------------ #


class Atendimento(models.Model):
    """ Classe Atendimento """

    realizado = models.BooleanField(default=False, help_text='Confirmação de Atendimento ocorrido')
    horario = models.DateTimeField(auto_now=False, auto_now_add=False)
    FK_atendido = models.ForeignKey(Cliente, verbose_name=("Cliente"), on_delete=models.CASCADE, related_name='app_Atendimento_Cliente', default=None)
    FK_modalidade = models.ForeignKey(Modalidade, verbose_name=("Modalidade"), on_delete=models.CASCADE, related_name='app_Atendimento_Modalidalde', default=None)

    class Meta:
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'

    # def __str__(self):
    #     return self.FK_atendido
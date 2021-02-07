# Generated by Django 3.1.6 on 2021-02-06 21:50

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('telefone', models.CharField(default=None, help_text='Campo obrigatorio*', max_length=11)),
                ('endereco', models.CharField(blank=True, max_length=254)),
                ('instagram', models.CharField(blank=True, max_length=50)),
                ('nascimento', models.DateField(default=None, help_text='Campo obrigatório*')),
                ('profissao', models.CharField(blank=True, choices=[('desempregado', 'Desempregado'), ('empregado', 'Empregado')], default='desempregado', max_length=20)),
                ('estado_civil', models.CharField(blank=True, choices=[('solteiro(a)', 'Solteiro(a)'), ('casado(a)', 'Casado(a)'), ('divorciado(a)', 'Divorciado(a)'), ('viúvo(a)', 'Viúvo(a)')], default='solterio(a)', max_length=20)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Modalidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modalidade', models.CharField(choices=[('', ''), ('Terapia', 'Terapia'), ('Tai Chi Chuan', 'Tai Chi Chuan'), ('Cone Hindu', 'Cone Hindu'), ('Barras de Access', 'Barras de Access')], default='', max_length=30, unique=True)),
                ('valor', models.FloatField(default=None, help_text='Campo obrigatório*')),
                ('tempo_duracao', models.DurationField(default=None, help_text='Campo obrigatório*')),
            ],
            options={
                'verbose_name': 'Modalidade',
                'verbose_name_plural': 'Modalidades',
            },
        ),
        migrations.CreateModel(
            name='Terapeuta',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('telefone', models.CharField(default=None, help_text='Campo obrigatorio*', max_length=11)),
                ('endereco', models.CharField(blank=True, max_length=254)),
                ('instagram', models.CharField(blank=True, max_length=50)),
                ('hora_entrada', models.TimeField(help_text='Entrada para o atendimento')),
                ('hora_alm_entrda', models.TimeField(help_text='Saida para almoço')),
                ('hora_alm_saida', models.TimeField(help_text='Retorno do horário de almoço')),
                ('hora_saida', models.TimeField(help_text='Horário de saida')),
            ],
            options={
                'verbose_name': 'Terapeuta',
                'verbose_name_plural': 'Terapeutas',
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realizado', models.BooleanField(default=False, help_text='Confirmação de Atendimento ocorrido')),
                ('horario', models.DateTimeField()),
                ('FK_atendido', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='app_Atendimento_Cliente', to='Espaco_Tao.cliente', verbose_name='Cliente')),
                ('FK_modalidade', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='app_Atendimento_Modalidalde', to='Espaco_Tao.modalidade', verbose_name='Modalidade')),
            ],
            options={
                'verbose_name': 'Atendimento',
                'verbose_name_plural': 'Atendimentos',
            },
        ),
    ]
from django.contrib import admin
from .models import Terapeuta, Cliente, Modalidade, Atendimento

@admin.register(Terapeuta)
class TerapeutaAdmin(admin.ModelAdmin):
    '''Admin View for Terapeuta'''

    list_display = ('first_name', 'is_staff', 'hora_entrada', 'hora_saida')
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    '''Admin View for Cliente'''

    list_display = ('first_name', 'username', 'is_active', 'nascimento')
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)

@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    '''Admin View for Modalidade'''

    list_display = ('modalidade', 'valor', 'tempo_duracao')
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)

@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    '''Admin View for Atendimento'''

    list_display = ('FK_atendido', 'FK_modalidade', 'realizado')
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)
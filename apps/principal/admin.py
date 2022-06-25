from django.contrib import admin
from .models import Contato, EmailNewsletter, MensagemContato

class ListandoContatos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'empresa', 'data', 'respondida')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'empresa')
    list_filter = ('respondida', 'data', 'empresa',)
    list_editable = ('respondida',)
    list_per_page = 10

class ListandoEmails(admin.ModelAdmin):
    list_display = ('id', 'email', 'data', 'ativo',)
    list_display_links = ('id', 'email',)
    search_fields = ('email', 'data',)
    list_filter = ('ativo', 'data',)
    list_editable = ('ativo',)
    list_per_page = 10

class ListandoMensagensContato(admin.ModelAdmin):
    list_display = ('nome', 'email', 'interesse', 'data', 'forma_contato', 'respondida',)
    list_display_links = ('nome', 'email',)
    search_fields = ('nome', 'email', 'data', 'interesse',)
    list_filter = ('interesse', 'data', 'respondida',)
    list_editable = ('respondida',)
    list_per_page = 10

admin.site.register(Contato, ListandoContatos)
admin.site.register(EmailNewsletter, ListandoEmails)
admin.site.register(MensagemContato, ListandoMensagensContato)
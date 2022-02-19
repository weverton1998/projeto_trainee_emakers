from django.contrib import admin

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .forms import (
    Edit_User_Admin,
    Create_User_Admin
)

User = get_user_model()

def remove_admin(modeladmin, request, queryset): 
    for user in queryset: #fazendo busca na listad e usuarios
        user.admin=False
        user.save()

remove_admin.short_description = 'Rebaixar usuários a membros'

def add_admin(modeladmin, request, queryset): 
    for user in queryset: #fazendo busca na listad e usuarios
        user.admin=True
        user.save()

add_admin.short_description = 'Promover usuários a administradores'

class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User
    #form que será utilziado para edição de usuário
    form = Edit_User_Admin
    # form para criação de novo usuário
    add_form = Create_User_Admin
    # utilizado para fazer busca de usuarios
    search_fields = ['firstname', 'lastname', 'email']
    list_display = ('nome_completo', 'email', 'gender', 'city', 'state',
                    'date_born', 'admin'
    )
    actions = ['remove_admin', 'add_admin']

    def nome_completo(self, obj):
        return obj.get_full_name()

    #usuario tem permissão para deletar outro
    def has_delete_permission(self, request, obj=None):
        return False

    # pega o formulário referente a ação do usuario
    def get_form(self, request, obj=None, **kwargs):
        # Usado na criação de um usuário
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, defaults)


admin.site.register(User, UserAdmin)

# Removendo o Model Group da listagem. Não é utilizado.
admin.site.unregister(Group)


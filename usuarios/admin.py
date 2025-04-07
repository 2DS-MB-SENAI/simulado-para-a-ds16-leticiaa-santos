from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(UserAdmin):

    # campos que serão mostrados quando exibir o usuário
    list_display = ('username', 'telefone',)

    # campos que serão necessários serem preenchidos, além dos que já estão pré-definidos
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('telefone',)}),
    )

    # adiciona outros campos além dos que já são padrão
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('telefone',)}),
    )

admin.site.register(User, UserAdmin)
from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'website', 'phone_number', 'picture')
    list_display_links = ('id', 'user')
    list_editable = ('website', 'phone_number')
    readonly_fields = ('created', 'modified', 'user')
    search_fields = (
        'id',
        'user__email',
        'user__first_name',
        'user__last_name',
        'website',
        'phone_number',
        'picture'
    )
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )
    fieldsets = (
        ('Perfil', {
            'fields':(
                ('user', 'picture',),
                ('phone_number',),

            ),  #al agrupar los campos en tuplas se muestran juntos
        }),
        ('Información extra', {
            'fields':(
                ('website',),
                ('biography',),
            ),
        }),
        ('Metadatos', {
            'fields':(
                ('created', 'modified',),
            )
        }),
    )
#Agregar crear el perfil junto con la creacion del usuario
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Perfiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
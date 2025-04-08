from django.contrib import admin
from . import models as user_models
from django.contrib.auth.admin import UserAdmin


@admin.register(user_models.User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('password',)}),
        (('Personal info'), {'fields': ('name','email','is_active', 'is_staff', 'is_superuser')}),
        (('Permissions'), {'fields': ('permissions',)}),
    )
    add_fieldsets = (
       
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'is_staff'),
        }),
    )
    search_fields = ('email',)
    list_display = ['id','name','email','is_active']
    list_filter = ['joined_date']
    list_display_links = ["id","name"]
    ordering = ('-id',)

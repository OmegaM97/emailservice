from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Client


class ClientAdmin(UserAdmin):
    model = Client
    list_display = ['username', 'email', 'is_staff']


admin.site.register(Client, ClientAdmin)

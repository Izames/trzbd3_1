from django.contrib import admin
from .models import *

@admin.register(Forge)
class ForgeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'price', 'available']
    list_display_links = ['pk', 'name']
    search_fields = ['name']
    list_editable = ('price', 'available')


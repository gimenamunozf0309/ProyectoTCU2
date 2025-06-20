from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import PeriodoTCU

@admin.register(PeriodoTCU)
class PeriodoTCUAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin', 'estado')  # Campos visibles en la lista
    list_filter = ('estado',)  # Filtro por estado
    search_fields = ('nombre',)  # Búsqueda posr nombre
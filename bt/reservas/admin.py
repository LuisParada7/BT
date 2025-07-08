from django.contrib import admin
from .models import TrainingType, TrainingReservation
from import_export.admin import ImportExportModelAdmin


@admin.register(TrainingType)
class TrainingTypeAdmin(ImportExportModelAdmin):
    list_display = ('name', 'description', 'image')
    search_fields = ('name', 'description')
    ordering = ['name']

@admin.register(TrainingReservation)
class TrainingReservationAdmin(ImportExportModelAdmin):
    list_display = ('user', 'date', 'time', 'location', 'display_training_types', 'phone', 'notes', 'completed',)
    list_filter = ('date', 'time', 'completed', 'user', 'training_type',)
    search_fields = ('user__username', 'user__email', 'date', 'location', 'phone', 'training_type__name')
    ordering = ['-date', '-time']

    def display_training_types(self, obj):
        """
        Crea una cadena con los nombres de los TrainingType asociados.
        """
        return ", ".join([tt.name for tt in obj.training_type.all()])
    display_training_types.short_description = "Tipos de Entrenamiento" # Nombre de la columna en el admin

    # Organizar los campos en el formulario de creación/edición
    fieldsets = (
        (None, { # Primera sección, sin título
            'fields': ('user', 'date', 'time', 'location')
        }),
        ('Detalles del Entrenamiento', {
            'fields': ('training_type', 'phone', 'notes') # training_type es M2M, se mostrará con el widget apropiado
        }),
        ('Estado', {
            'fields': ('completed',)
        }),
    )
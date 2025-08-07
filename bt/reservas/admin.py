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
    list_display = ('user', 'date', 'time', 'location', 'display_training_type', 'phone', 'notes', 'completed',)
    list_filter = ('date', 'completed', 'user', 'training_type',)
    search_fields = ('user__username', 'user__email', 'location', 'training_type__name')
    ordering = ['-date', '-time']

    def display_training_type(self, obj):
        """
        Muestra el nombre del TrainingType asociado.
        """
        # Primero, comprueba si la reserva tiene un tipo de entrenamiento asignado
        if obj.training_type:
            # Si lo tiene, devuelve su nombre. Ya no se necesita .all()
            return obj.training_type.name
        # Si no tiene ninguno, devuelve un texto por defecto
        return "Sin asignar"

    # Cambiamos la descripción para que coincida con el nuevo nombre
    display_training_type.short_description = "Tipo de Entrenamiento"# Nombre de la columna en el admin

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
from django import forms
from .models import TrainingReservation

class TrainingReservationForm(forms.ModelForm):
    class Meta:
        model = TrainingReservation
        fields = ['date', 'time', 'location', 'training_type', 'phone', 'notes',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Opcional: Añadir clases de CSS o placeholders a los campos
        self.fields['location'].widget.attrs.update({'placeholder': 'Dirección o parque'})
        self.fields['phone'].widget.attrs.update({'placeholder': 'Ej: 3001234567'})
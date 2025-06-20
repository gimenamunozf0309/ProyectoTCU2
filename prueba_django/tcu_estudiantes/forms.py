from django import forms
from .models import TCUEstudiante

class TCUEstudianteForm(forms.ModelForm):
    class Meta:
        model = TCUEstudiante
        fields = ['nombre', 'identificacion', 'carnet', 'correo', 'telefono',
                  'lugar_tcu', 'encargado', 'fecha_solicitud', 'estado', 'observaciones', 'documento']
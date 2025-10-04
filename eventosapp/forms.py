from django import forms
from .models import Evento, Participante
from datetime import date

#form evento
class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'fecha', 'ubicacion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
        }

    #validar fecha futura
    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha <= date.today():
            raise forms.ValidationError("La fecha debe ser futura")
        return fecha

#form participante
class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        fields = ['nombre', 'email']
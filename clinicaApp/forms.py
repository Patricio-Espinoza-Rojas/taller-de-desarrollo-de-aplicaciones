from django import forms
from .models import Agenda, Receta
from django.forms.widgets import DateInput


class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['id_agenda', 'dia', 'hora'] 
        widgets = {
            'dia': DateInput(attrs={'type': 'date'}),
        }


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['id_receta', 'fecha','sexo','edad','instrucciones','medicamentos','rutPaciente']
        widgets = {
            'fecha': DateInput(attrs={'type': 'date'}),
        }

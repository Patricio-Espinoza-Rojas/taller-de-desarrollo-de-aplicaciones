from django import forms
from .models import Agenda, Receta

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['id_agenda', 'dia', 'hora'] 

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['id_receta', 'fecha','sexo','instrucciones','medicamentos','rutPaciente']

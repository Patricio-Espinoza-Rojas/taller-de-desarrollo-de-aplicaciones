from dataclasses import dataclass
from datetime import datetime

@dataclass
class FichaPacienteDAO:
    idFicha: int
    anamnesis: str
    diagnostico: str
    fecha: datetime
    rutPaciente : str
    idDoctor: int
    idEspecialidad: int
    idReceta: int
from dataclasses import dataclass
from datetime import datetime

@dataclass 
class recetaDAO:
    idReceta: int
    medicamentos: str
    fecha: datetime 
    rutPaciente: str
    idDoctor: int
    
from dataclasses import dataclass

@dataclass
class doctorDAO:
    idDoctor: int
    nombreDoctor:str
    titulo:str
    correo: str
    idEspecialidad: int
    idAgenda: int
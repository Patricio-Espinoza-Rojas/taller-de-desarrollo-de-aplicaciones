from dataclasses import dataclass

@dataclass
class pacienteDAO:
    rutPaciente: str
    nombrePaciente: str
    direccion: str
    telefono: str
    correo: str
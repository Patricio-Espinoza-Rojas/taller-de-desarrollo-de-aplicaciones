from dataclasses import dataclass
from datetime import datetime


@dataclass
class agendaDAO:
    idAgenda:int
    dia: datetime
    hora:int
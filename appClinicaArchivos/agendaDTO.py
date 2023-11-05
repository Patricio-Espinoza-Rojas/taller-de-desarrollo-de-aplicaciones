from logging import exception
from mysql import connector
from agendaDAO import agendaDAO    



class AgendaDTO:
    
    @staticmethod
    def conectar():
        conector = connector.connect(database='centromedico', user='root')
        return conector
    
    def ingresarAgenda(self, agenda:agendaDAO):
        try:
            sql = 'insert into Agenda values(%s,%s,%s)'
            con = AgendaDTO.conectar()
            cursor = con.cursor()
            cursor.execute(sql,[agenda.idAgenda, agenda.dia, agenda.hora])
            con.commit()
            con.close()
        except Exception as ex:
            return ex
        
    def eliminarAgenda(self, agenda:agendaDAO):
        try:
            sql = 'delete from Agenda where ID_agenda = %s'
            con = AgendaDTO.conectar()
            cursor = con.cursor()
            cursor.execute(sql,[agenda.idAgenda])
            con.commit()
            con.close()
        except exception as ex:
            return ex        
        
    def actualizarAgenda(self, agenda:agendaDAO):
        try: 
            sql = 'update Agenda set dia = %s, hora = %s where ID_agenda = %s'
            con = AgendaDTO.conectar() 
            cursor = con.cursor()
            cursor.execute(sql,[agenda.idAgenda, agenda.dia, agenda.hora])
            con.commit()
            con.close()
        except Exception as ex:
            return ex    

    def listarAgenda(self):
        try:
            sql = 'select * from `Agenda`'
            con = AgendaDTO.conectar()
            cursor= con.cursor()
            cursor.execute(sql)
            resultados = cursor.fetchall()
            con.commit()
            con.close()
            filas = list()
            for registro in resultados:
                ag = agendaDAO(registro[0], registro[1], registro[2])
                filas.append(ag)
            return filas
        except Exception as ex:
            return ex

    def buscarAgenda(self, agenda:agendaDAO):
        try:
            sql = 'select * from Agenda where ID_agenda like %s'
            con = AgendaDTO.conectar()
            cursor = con.cursor()
            cursor.execute(sql,[agenda.idAgenda])
            resultado = cursor.fetchone()
            con.commit()
            con.close()
            age = agendaDAO(resultado[0],resultado[1], resultado[2])
            return age
        except Exception as ex:
            return ex
            

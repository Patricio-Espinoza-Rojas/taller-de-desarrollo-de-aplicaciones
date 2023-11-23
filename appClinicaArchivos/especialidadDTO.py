from logging import exception
from mysql import connector
from especialidadDAO import especialidadDAO    



class EspecialidadDTO:
    
    @staticmethod
    def conectar():
        conector = connector.connect(database='centromedico', user='root')
        return conector
    
    def ingresarEspecialidad(self, especialidad:especialidadDAO):
        try:
            sql = 'insert into Especialidad values(%s,%s)'
            con = EspecialidadDTO.conectar()
            cursor = con.cursor()
            cursor.execute(sql,[especialidad.idEspecialidad, especialidad.nombreEspecialidad])
            con.commit()
            con.close()
        except Exception as ex:
            return ex
        
    def eliminarEspecialidad(self,especialidad:especialidadDAO):
        try:
            sql = 'delete from Especialidad where ID_especialidad = %s'
            con = EspecialidadDTO.conectar()
            cursor = con.cursor()
            cursor.execute(sql,[especialidad.idEspecialidad])
            con.commit()
            con.close()
        except exception as ex:
            return ex        
        
    def actualizarEspecialidad(self,especialidad:especialidadDAO):
        try: 
            sql = 'update Especialidad set nombreEspecialidad = %s where ID_especialidad = %s'
            con = EspecialidadDTO.conectar() 
            cursor = con.cursor()
            cursor.execute(sql,[especialidad.idEspecialidad, especialidad.nombreEspecialidad])
            con.commit()
            con.close()
        except Exception as ex:
            return ex    

    def listarEspecialidad(self):
        try:
            sql = 'select * from `Especialidad`'
            con = EspecialidadDTO.conectar()
            cursor= con.cursor()
            cursor.execute(sql)
            resultados = cursor.fetchall()
            con.commit()
            con.close()
            filas = list()
            for registro in resultados:
                es = especialidadDAO(registro[0], registro[1])
                filas.append(es)
            return filas
        except Exception as ex:
            return ex

    def buscarEspecialidad(self,especialidad:especialidadDAO):
        try:
            sql = 'select * from Especialidad where ID_especialidad like %s'
            con = EspecialidadDTO.conectar()
            cursor = con.cursor()
            cursor.execute(sql,[especialidad.idEspecialidad])
            resultado = cursor.fetchone()
            con.commit()
            con.close()
            espe = especialidadDAO(resultado[0],resultado[1])
            return espe
        except Exception as ex:
            return ex
            

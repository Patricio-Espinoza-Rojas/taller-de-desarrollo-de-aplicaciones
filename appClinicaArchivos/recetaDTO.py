from logging import exception
from mysql import connector
from recetaDAO import recetaDAO    



class RecetaDTO:
    
    @staticmethod
    def conectar():
        conector = connector.connect(database='centromedico', user='root')
        return conector
    
    def ingresarReceta(self, receta:recetaDAO):
        try:
            sql = 'insert into receta values(%s,%s,%s,%s,%s)'
            con = RecetaDTO.conectar()
            cursor = con.cursor()
            cursor.execute(sql,[receta.idReceta, receta.medicamentos, receta.fecha, 
                                receta.rutPaciente, receta.idDoctor])
            con.commit()
            con.close()
        except Exception as ex:
            return ex
        
    def eliminarReceta(self,receta:recetaDAO):
        try:
            sql = 'delete from Receta where ID_receta = %s'
            con = RecetaDTO.conectar()
            cursor = con.cursor()
            cursor.execute(sql,[receta.idReceta])
            con.commit()
            con.close()
        except exception as ex:
            return ex        
        
    def actualizarReceta(self,receta:recetaDAO):
        try: 
            sql = 'update Receta set medicamentos = %s, fecha = %s, RUT_paciente = %s, ID_doctor = %s where ID_receta = %s'
            con = RecetaDTO.conectar() 
            cursor = con.cursor()
            cursor.execute(sql,[receta.idReceta, receta.medicamentos, receta.fecha, receta.rutPaciente, receta.idDoctor])
            con.commit()
            con.close()
        except Exception as ex:
            return ex    

    def listarReceta(self):
        try:
            sql = 'select * from `receta`'
            con = RecetaDTO.conectar()
            cursor= con.cursor()
            cursor.execute(sql)
            resultados = cursor.fetchall()
            con.commit()
            con.close()
            filas = list()
            for registro in resultados:
                re = recetaDAO(registro[0], registro[1], registro[2], registro[3], registro[4])
                filas.append(re)
            return filas
        except Exception as ex:
            return ex

    def buscarReceta(self,receta:recetaDAO):
        try:
            sql = 'select * from Receta where ID_receta like %s'
            con = RecetaDTO.conectar()
            cursor = con.cursor()
            cursor.execute(sql,[receta.idReceta])
            resultado = cursor.fetchone()
            con.commit()
            con.close()
            rece = recetaDAO(resultado[0],resultado[1], resultado[2], resultado[3],resultado[4])
            return rece
        except Exception as ex:
            return ex
            

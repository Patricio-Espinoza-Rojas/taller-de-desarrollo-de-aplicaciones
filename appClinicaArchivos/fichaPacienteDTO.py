from logging import exception
from mysql import connector
from fichaPacienteDAO import FichaPacienteDAO


class FichaPacienteDTO:
    
    @staticmethod
    def conectar():
        conector = connector.connect(database='centromedico', user='root')
        return conector
    
    def ingresarFicha(self, ficha:FichaPacienteDAO):
        try:
            sql = 'insert into fichaclinicapaciente values(%s,%s,%s,%s,%s,%s,%s,%s)'
            con = FichaPacienteDTO.conectar()
            cursor = con.cursor()
            cursor.execute(sql,[ficha.idFicha, ficha.anamnesis, ficha.diagnostico, 
                                ficha.fecha, ficha.rutPaciente, ficha.idDoctor, ficha.idEspecialidad, ficha.idReceta])
            con.commit()
            con.close()
        except Exception as ex:
            return ex
        
    def eliminarFicha(self,ficha:FichaPacienteDAO):
        try:
            sql = 'delete from fichaclinicapaciente where ID_ficha = %s'
            con = FichaPacienteDTO.conectar()
            cursor = con.cursor()
            cursor.execute(sql,[ficha.idFicha])
            con.commit()
            con.close()
        except exception as ex:
            return ex        
        
    def actualizarFicha(self,ficha:FichaPacienteDAO):
        try: 
            sql = 'update fichaclinicapaciente set anamnesis = %s, diagnostico = %s, fecha = %s, RUT_paciente = %s, ID_doctor = %s, ID_especialidad = %s, ID_receta = %s where ID_ficha = %s'
            con = FichaPacienteDTO.conectar() 
            cursor = con.cursor()
            cursor.execute(sql,[ficha.idFicha, ficha.anamnesis, ficha.diagnostico, 
                                ficha.fecha, ficha.rutPaciente, ficha.idDoctor, ficha.idEspecialidad, ficha.idReceta])
            con.commit()
            con.close()
        except Exception as ex:
            return ex    

    def listarFicha(self):
        try:
            sql = 'select * from `fichaclinicapaciente`'
            con = FichaPacienteDTO.conectar()
            cursor= con.cursor()
            cursor.execute(sql)
            resultados = cursor.fetchall()
            con.commit()
            con.close()
            filas = list()
            for registro in resultados:
                fi = FichaPacienteDAO(registro[0], registro[1], registro[2], registro[3], registro[4],registro[5], registro[6], registro[7])
                filas.append(fi)
            return filas
        except Exception as ex:
            return ex

    def buscarFicha(self,ficha:FichaPacienteDAO):
        try:
            sql = 'select * from fichaclinicapaciente where ID_ficha like %s'
            con = FichaPacienteDTO.conectar()
            cursor = con.cursor()
            cursor.execute(sql,[ficha.idFicha])
            resultado = cursor.fetchone()
            con.commit()
            con.close()
            fic = FichaPacienteDAO(resultado[0],resultado[1], resultado[2], resultado[3],resultado[4], resultado[5], resultado[6], resultado[7])
            return fic
        except Exception as ex:
            return ex
            


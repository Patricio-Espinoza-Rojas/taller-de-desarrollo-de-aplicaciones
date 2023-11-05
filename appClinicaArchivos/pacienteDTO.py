from logging import exception
from mysql import connector
from pacienteDAO import pacienteDAO    



class PacienteDTO:
    
    @staticmethod
    def conectar():
        conector = connector.connect(database='centromedico', user='root')
        return conector
    
    def ingresarPaciente(self, paciente:pacienteDAO):
        try:
            sql = 'insert into paciente values(%s,%s,%s,%s,%s)'
            con = PacienteDTO.conectar()
            cursor = con.cursor()
            cursor.execute(sql,[paciente.rutPaciente, paciente.nombrePaciente, paciente.direccion, 
                                paciente.telefono, paciente.correo])
            con.commit()
            con.close()
        except Exception as ex:
            return ex
        
    def eliminarPaciente(self,paciente:pacienteDAO):
        try:
            sql = 'delete from paciente where RUT_paciente = %s'
            con = PacienteDTO.conectar()
            cursor = con.cursor()
            cursor.execute(sql,[paciente.rutPaciente])
            con.commit()
            con.close()
        except exception as ex:
            return ex        
        
    def actualizarPaciente(self,paciente:pacienteDAO):
        try: 
            sql = 'update paciente set nombrePaciente = %s, direccion = %s, telefono = %s, correo = %s where RUT_paciente = %s'
            con = PacienteDTO.conectar() 
            cursor = con.cursor()
            cursor.execute(sql,[paciente.rutPaciente,paciente.nombrePaciente,paciente.direccion, paciente.telefono, paciente.correo])
            con.commit()
            con.close()
        except Exception as ex:
            return ex    

    def listarPacientes(self):
        try:
            sql = 'select * from `paciente`'
            con = PacienteDTO.conectar()
            cursor= con.cursor()
            cursor.execute(sql)
            resultados = cursor.fetchall()
            con.commit()
            con.close()
            filas = list()
            for registro in resultados:
                pa = pacienteDAO(registro[0], registro[1], registro[2], registro[3], registro[4])
                filas.append(pa)
            return filas
        except Exception as ex:
            return ex

    def buscarPaciente(self,paciente:pacienteDAO):
        try:
            sql = 'select * from paciente where RUT_paciente like %s'
            con = PacienteDTO.conectar()
            cursor = con.cursor()
            cursor.execute(sql,[paciente.rutPaciente])
            resultado = cursor.fetchone()
            con.commit()
            con.close()
            pacie = pacienteDAO(resultado[0],resultado[1], resultado[2], resultado[3],resultado[4])
            return pacie
        except Exception as ex:
            return ex
            

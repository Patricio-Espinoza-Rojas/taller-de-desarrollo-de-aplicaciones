from logging import exception
from mysql import connector
from doctorDAO import doctorDAO    



class DoctorDTO:
    
    @staticmethod
    def conectar():
        conector = connector.connect(database='centromedico', user='root')
        return conector
    
    def ingresarDoctor(self, doctor:doctorDAO):
        try:
            sql = 'insert into Doctores values(%s,%s,%s,%s,%s,%s)'
            con = DoctorDTO.conectar()
            cursor = con.cursor()
            cursor.execute(sql,[doctor.idDoctor, doctor.nombreDoctor, doctor.titulo, 
                                doctor.correo, doctor.idEspecialidad, doctor.idAgenda])
            con.commit()
            con.close()
        except Exception as ex:
            return ex
        
    def eliminarDoctor(self, doctor:doctorDAO):
        try:
            sql = 'delete from Doctores where ID_doctor = %s'
            con = DoctorDTO.conectar()
            cursor = con.cursor()
            cursor.execute(sql,[doctor.idDoctor])
            con.commit()
            con.close()
        except exception as ex:
            return ex        
        
    def actualizarDoctor(self, doctor:doctorDAO):
        try: 
            sql = 'update Doctores set nombreDoctor = %s, titulo = %s, correo = %s, ID_especialidad = %s, ID_agenda = %s where ID_doctor = %s'
            con = DoctorDTO.conectar() 
            cursor = con.cursor()
            cursor.execute(sql,[doctor.idDoctor, doctor.nombreDoctor, doctor.titulo, 
                                doctor.correo, doctor.idEspecialidad, doctor.idAgenda])
            con.commit()
            con.close()
        except Exception as ex:
            return ex    

    def listarDoctor(self):
        try:
            sql = 'select * from `Doctores`'
            con = DoctorDTO.conectar()
            cursor= con.cursor()
            cursor.execute(sql)
            resultados = cursor.fetchall()
            con.commit()
            con.close()
            filas = list()
            for registro in resultados:
                doc = doctorDAO(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
                filas.append(doc)
            return filas
        except Exception as ex:
            return ex

    def buscarDoctor(self, doctor:doctorDAO):
        try:
            sql = 'select * from Doctores where ID_doctor like %s'
            con = DoctorDTO.conectar()
            cursor = con.cursor()
            cursor.execute(sql,[doctor.idDoctor])
            resultado = cursor.fetchone()
            con.commit()
            con.close()
            docto = doctorDAO(resultado[0],resultado[1], resultado[2], resultado[3],resultado[4], resultado[5])
            return docto
        except Exception as ex:
            return ex
            

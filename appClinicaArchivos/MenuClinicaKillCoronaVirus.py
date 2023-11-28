# -*- coding: utf-8 -*-
import os
from pacienteDAO import pacienteDAO
from pacienteDTO import PacienteDTO
from fichaPacienteDAO import FichaPacienteDAO
from fichaPacienteDTO import FichaPacienteDTO
from recetaDAO import recetaDAO
from recetaDTO import RecetaDTO
from doctorDAO import doctorDAO
from doctorDTO import DoctorDTO
from agendaDAO import agendaDAO
from agendaDTO import AgendaDTO
from especialidadDAO import especialidadDAO
from especialidadDTO import EspecialidadDTO


def main_menu():
    print("=== Menú Principal ===")
    print("1. Paciente")
    print("2. Ficha clínica paciente")
    print("3. Doctor")
    print("4. Especialidad")
    print("5. Agenda")
    print("6. Receta")
    print("0. Salir")

def paciente_submenu():
    print("=== Submenú Paciente ===")
    print("1. Ingresar paciente")
    print("2. Eliminar paciente")
    print("3. Actualizar paciente")
    print("4. Listar pacientes")
    print("5. Buscar paciente")
    print("0. Volver al Menú Principal")
    
def fichapaciente_submenu():
    print("=== Submenú Ficha Paciente ===")
    print("1. Ingresar Ficha Paciente")
    print("2. Eliminar Ficha Paciente")
    print("3. Actualizar Ficha Paciente")
    print("4. Listar Ficha Paciente")
    print("5. Buscar Ficha Paciente")
    print("0. Volver al Menú Principal")

def doctor_submenu():
    print("=== Submenú Doctor ===")
    print("1. Ingresar Doctor")
    print("2. Eliminar Doctor")
    print("3. Actualizar Doctores")
    print("4. Listar Doctores")
    print("5. Buscar Doctor")
    print("0. Volver al Menú Principal")    

def especialidad_submenu():
    print("=== Submenú Especialidad ===")
    print("1. Ingresar Especialidad")
    print("2. Eliminar Especialidad")
    print("3. Actualizar Especialidad")
    print("4. Listar Especialidad")
    print("5. Buscar Especialidad")
    print("0. Volver al Menú Principal")

def agenda_submenu():
    print("=== Submenú Agenda ===")
    print("1. Ingrese fecha para agendar")
    print("2. Eliminar fecha agendada")
    print("3. Actualizar Agenda")
    print("4. Listar Agenda")
    print("5. Buscar fecha agendada")
    print("0. Volver al Menú Principal")


def receta_submenu():
    print("=== Submenú Receta ===")
    print("1. Ingresar Receta")
    print("2. Eliminar Receta")
    print("3. Actualizar Receta")
    print("4. Listar Receta")
    print("5. Buscar Receta")
    print("0. Volver al Menú Principal")


aceptar_terminos = False

while not aceptar_terminos:
    texto = """****
    Este es un desarrollo solicitado por Clínica Kill Corona Virus
    para ser ejecutado por Leonardo Godoy, Patricio Espinoza y Alejandro Valenzuela .
    Se prohíbe estrictamente su uso malintencionado, comercialización, adulteración y/o reproducción
    sin el consentimiento de las personas anteriormente señaladas.
    La mala calificación de este trabajo será penalizada con un lag de 100 años.****"""
    print(texto)
    print("")
   
    print("------ ¡Bienvenido a Clínica Killcorona! ------")
    print("------------Términos y Condiciones -----------")
    print("Por favor, selecciona una opción para continuar: \n")
    print("Presiona el número 1 para aceptar los términos y condiciones y proceder con\nel uso de nuestra aplicación.\n")
    print("Presiona el número 2 si no deseas aceptar los términos y condiciones y \nabandonar la aplicación.\n")
    print("1.Aceptar")
    print("2.Rechazar\n")      
    
    opcion_terminos = input("Seleccione una opción para aceptar o rechazar los términos: ")
    
    
    if opcion_terminos == "1":
        aceptar_terminos = True 
 
    else:
        aceptar_terminos = False
        os.system("cls")
        print("Se rechazan los terminos\n")
        input("presione enter para continuar....")
        break
        

    def main():
        while True:
            os.system("cls")
            main_menu()
            choice = input("Selecciona una opción: ")

            if choice == "0":
                break
            elif choice == "1":
                dto = PacienteDTO()
                os.system("cls")
                while True:
                    
                    paciente_submenu()
                    choice = input("Selecciona una opción: ")
                    os.system("cls")

                    if choice == "0":
                        break
                    elif choice == "1":
                        # Ingresar paciente
                        
                        rutPaciente = input("Ingrese el RUT del paciente: ")
                        nombrePaciente = input("Ingrese el nombre del paciente: ")
                        direccion = input("Ingrese la dirección del paciente: ")
                        telefono = input("Ingrese el teléfono del paciente: ")
                        correo = input("Ingrese el correo del paciente: ")

                        paciente = pacienteDAO(rutPaciente, nombrePaciente, direccion, telefono, correo)
                        dto.ingresarPaciente(paciente)
                        print("")
                        print("Paciente ingresado exitosamente.")
                        input("Presione enter para volver...")
                        os.system("cls")
                        pass
                    elif choice == "2":
                        # Eliminar paciente
                        
                        rutPaciente = input("Ingrese el RUT del paciente a eliminar: ")
                        paciente = pacienteDAO(rutPaciente, '', '', '', '')

                        if dto.buscarPaciente(paciente):
                            confirmacion = input("¿Está seguro de que desea eliminar el paciente ingresado? (si/no): ")

                            if confirmacion.lower() == "si":
                                dto.eliminarPaciente(paciente)
                                print("El paciente ha sido eliminado exitosamente.")
                            else:
                                print("La eliminación del paciente ha sido cancelada.")
                        else:
                            print("Error: El paciente ingresado no existe.")
                        print("")   
                        input("Presione enter para continuar")
                        os.system("cls")
                        pass
                        
                    elif choice == "3":
                        # Actualizar paciente
                        
                        rutPaciente = input("Ingrese el RUT del paciente a actualizar: ")
                        nombrePaciente = input("Ingrese el nuevo nombre del paciente: ")
                        direccion = input("Ingrese la nueva dirección del paciente: ")
                        telefono = input("Ingrese el nuevo teléfono del paciente: ")
                        correo = input("Ingrese el nuevo correo del paciente: ")
                        
                        paciente = pacienteDAO(nombrePaciente, direccion, telefono, correo,rutPaciente)
                        dto.actualizarPaciente(paciente)
                        print("")
                        print("Paciente actualizado exitosamente.")
                        input("Presion enter para volver para contnuar...")
                        os.system("cls")
                        pass
                    elif choice == "4":
                        # Listar paciente
                        
                        pacientes = dto.listarPacientes()
                        for paciente in pacientes:
                            print(f"RUT: {paciente.rutPaciente}, Nombre: {paciente.nombrePaciente}, Dirección: {paciente.direccion}, Teléfono: {paciente.telefono}, Correo: {paciente.correo}")
                        pass
                        print("")
                        input("Presion enter para volver para contnuar...")
                        os.system("cls")
                    elif choice == "5":
                        # Buscar paceinte
                        
                        rutPaciente = input("Ingrese el RUT del paciente a buscar: ")
                        paciente = pacienteDAO(rutPaciente, '', '', '', '')
                        resultado = dto.buscarPaciente(paciente)

                        if resultado:
                            print(f"RUT: {resultado.rutPaciente}, Nombre: {resultado.nombrePaciente}, Dirección: {resultado.direccion}, Teléfono: {resultado.telefono}, Correo: {resultado.correo}")
                        else:
                            print("El paciente ingresado no existe.")

                        pass
                        input("Presion enter para volver para contnuar...")
                        os.system("cls")
                    else:
                        print("Opción inválida. Por favor, intenta nuevamente.")

            elif choice == "2":
                dto = FichaPacienteDTO()
                while True:
                    os.system("cls")
                    fichapaciente_submenu()
                    choice = input("Selecciona una opción: ")
                    os.system("cls")

                    if choice == "0":
                        break
                    elif choice == "1":
                        #Insertar Ficha
                        
                        idFicha = input("Ingrese el ID de la ficha: ")
                        anamnesis = input("Ingrese la anamnesis: ")
                        diagnostico = input("Ingrese el diagnóstico: ")
                        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
                        rutPaciente = input("Ingrese el RUT del paciente: ")
                        idDoctor = input("Ingrese el ID del doctor: ")
                        idEspecialidad = input("Ingrese el ID de la especialidad del doctor: ")
                        idReceta = input("Ingrese el ID de la receta: ")

                        ficha = FichaPacienteDAO(idFicha, anamnesis, diagnostico, fecha, rutPaciente, idDoctor, idEspecialidad, idReceta)
                        dto.ingresarFicha(ficha)
                        print("")
                        print("Ficha ingresada exitosamente.")
                        input("Presione enter para continuar")
                        os.system("cls")
                        pass
                    elif choice == "2":
                        #Eliminar ficha
                        
                        idFicha = input("Ingrese el ID de la ficha a eliminar: ")
                        ficha = FichaPacienteDAO(idFicha, '', '', '', '', '', '', '')

                        if dto.buscarFicha(ficha):
                            confirmacion = input("¿Está seguro de que desea eliminar la ficha ingresada? (si/no): ")

                            if confirmacion.lower() == "si":
                                dto.eliminarFicha(ficha)
                                print("La ficha ha sido eliminada exitosamente.")
                            else:
                                print("La eliminación de la ficha ha sido cancelada.")
                        else:
                            print("Error: La ficha ingresada no existe.")
                        print("")
                        input("Presione enter para continuar")
                        pass
                    elif choice == "3":
                        # Actualizar ficha
                        
                        idFicha = input("Ingrese el ID de la ficha a actualizar: ")
                        anamnesis = input("Ingrese la nueva anamnesis: ")
                        diagnostico = input("Ingrese el nuevo diagnóstico: ")
                        fecha = input("Ingrese la nueva fecha (YYYY-MM-DD): ")
                        rutPaciente = input("Ingrese el nuevo RUT del paciente: ")
                        idDoctor = input("Ingrese el nuevo ID del doctor: ")
                        idEspecialidad = input("Ingrese el nuevo ID de la especialidad: ")
                        idReceta = input("Ingrese el nuevo ID de la receta: ")

                        ficha = FichaPacienteDAO(anamnesis, diagnostico, fecha, rutPaciente, idDoctor, idEspecialidad, idReceta,idFicha)
                        dto.actualizarFicha(ficha)
                        print("Ficha actualizada exitosamente.")
                        print("")
                        input("Presione enter para continuar...")
                        pass
                    
                    elif choice == "4":
                        #Listar ficha
                        
                        fichas = dto.listarFicha()
                        for ficha in fichas:
                            print(f"ID: {ficha.idFicha}, Anamnesis: {ficha.anamnesis}, Diagnóstico: {ficha.diagnostico}, Fecha: {ficha.fecha}, RUT Paciente: {ficha.rutPaciente}, ID Doctor: {ficha.idDoctor}, ID Especialidad: {ficha.idEspecialidad}, ID Receta: {ficha.idReceta}")
                        pass
                        print("")
                        input("Presion enter para volver para contnuar...")
                        os.system("cls")
                        
                    elif choice == "5":
                        #Buscar ficha
                        
                        idFicha = input("Ingrese el ID de la ficha a buscar: ")
                        ficha = FichaPacienteDAO(idFicha, '', '', '', '', '', '', '')
                        resultado = dto.buscarFicha(ficha)

                        if resultado:
                            print(f"ID: {resultado.idFicha}, Anamnesis: {resultado.anamnesis}, Diagnóstico: {resultado.diagnostico}, Fecha: {resultado.fecha}, RUT Paciente: {resultado.rutPaciente}, ID Doctor: {resultado.idDoctor}, ID Especialidad: {resultado.idEspecialidad}, ID Receta: {resultado.idReceta}")
                        else:
                            print("La ficha ingresada no existe.")
                        pass
                        input("Presion enter para volver para contnuar...")
                        os.system("cls")
                    else:
                        print("Opción inválida. Por favor, intenta nuevamente.")   
        
            elif choice == "3":
                dto = DoctorDTO()
                while True:
                    os.system("cls")
                    doctor_submenu()
                    choice = input("Selecciona una opción: ")
                    os.system("cls")

                    if choice == "0":
                        break
                    elif choice == "1":
                        # Ingresar doctor
                        
                        idDoctor= input("Ingrese el ID del doctor: ")
                        nombreDoctor = input("Ingrese el nombre del doctor: ")
                        titulo = input("Ingrese el titulo del doctor: ")
                        correo = input("Ingrese el correo del doctor: ")
                        idEspecialidad = input("Ingrese la id de especialidad: ")
                        idAgenda = input("Ingrese la id de agenda: ")

                        doctor = doctorDAO(idDoctor, nombreDoctor, titulo, correo, idEspecialidad, idAgenda)
                        dto.ingresarDoctor(doctor)
                        print("")
                        print("Doctor ingresado exitosamente.")
                        input("Presione enter para volver...")
                        os.system("cls")
                        pass
                                                
                    elif choice == "2":
                        # Eliminar doctor
                        
                        idDoctor = input("Ingrese el ID del doctor a eliminar: ")
                        doctor = doctorDAO(idDoctor, '', '', '', '','')

                        if dto.buscarDoctor(doctor):
                            confirmacion = input("¿Está seguro de que desea eliminar al doctor? (si/no): ")

                            if confirmacion.lower() == "si":
                                dto.eliminarDoctor(doctor)
                                print("El doctor se elimino exitosamente.")
                            else:
                                print("La eliminación del doctor ha sido cancelada.")
                        else:
                            print("Error: el Id del doctor  no existe.")
                        pass 
                        
                        input("Presion enter para volver para contnuar...")
                        os.system("cls")
                        
                    elif choice == "3":
                        # Actualizar doctor
                        
                        idDoctor = input("Ingrese el ID del doctor a actualizar: ")
                        nombreDoctor = input("Ingrese el nombre del doctor: ")
                        titulo = input("Ingrese el nuevo titulo: ")
                        correo = input("Ingrese el nuevo correo: ")
                        idEspecialidad = input("Ingrese el nuevo ID de la especialidad: ")
                        idAgenda = input("Ingrese el nuevo ID de agenda: ")

                        doctor = doctorDAO(nombreDoctor, titulo, correo, idEspecialidad, idAgenda, idDoctor)
                        dto.actualizarDoctor(doctor)
                        print("Doctor actualizado exitosamente.")
                                                
                        pass
                        input("Presion enter para volver para contnuar...")
                        os.system("cls") 
                                           
                    elif choice == "4":
                        # Listar Doctor
                        
                        doctores = dto.listarDoctor()
                        for doctor in doctores:
                            print(f"ID doctor: {doctor.idDoctor}, Nombre Doctor: {doctor.nombreDoctor}, Título: {doctor.titulo}, Correo: {doctor.correo}, Especialidad: {doctor.idEspecialidad}, Agenda: {doctor.idAgenda}")
                        
                        pass
                        print("")
                        input("Presion enter para volver para contnuar...")
                        os.system("cls")                        
                                                                   
                    elif choice == "5":
                        # Buscar doctor
                        
                        idDoctor = input("Ingrese el ID del doctor a buscar: ")
                        doctor = doctorDAO(idDoctor, '', '', '', '', '')
                        resultado = dto.buscarDoctor(doctor)

                        if resultado:
                            print(f"ID doctor: {resultado.idDoctor}, Nombre Doctor: {resultado.nombreDoctor}, Título: {resultado.titulo}, Correo: {resultado.correo}, Especialidad: {resultado.idEspecialidad}, Agenda: {resultado.idAgenda}")
                        else:
                            print("La Id de doctor ingresada no existe.")
                            
                        pass
                        input("Presion enter para volver para contnuar...")
                        os.system("cls")               
                    else:
                        print("Opción inválida. Por favor, intenta nuevamente.")  
            
            elif choice == "4":
                dto = EspecialidadDTO()
                while True:
                    os.system("cls")
                    especialidad_submenu()
                    choice = input("Selecciona una opción: ")
                    os.system("cls")

                    if choice == "0":
                        break
                    elif choice == "1":
                        # Ingresar especialidad
                        idEspecialidad = input("Ingrese el ID de la especialidad: ")
                        nombreEspecialidad = input("Ingrese el nombre de la especialidad: ")

                        especialidad = especialidadDAO(idEspecialidad, nombreEspecialidad)
                        dto.ingresarEspecialidad(especialidad)
                        print("Especialidad ingresada exitosamente.")
                        pass
                        input("Presion enter para volver para contnuar...")
                        os.system("cls")  
                                          
                    elif choice == "2":
                        # Eliminarespecialidad

                        idEspecialidad = input("Ingrese el ID de la especialidad a eliminar: ")
                        especialidad = especialidadDAO(idEspecialidad, '')

                        if dto.buscarEspecialidad(especialidad):
                            confirmacion = input("¿Está seguro de que desea eliminar la especialidad ingresada? (si/no): ")

                            if confirmacion.lower() == "si":
                                dto.eliminarEspecialidad(especialidad)
                                print("La especialidad ha sido eliminada exitosamente.")
                            else:
                                print("La eliminación de la especialidad ha sido cancelada.")
                        else:
                            print("Error: La especialidad ingresada no existe.")                        
                        pass
                        input("Presion enter para volver para contnuar...")
                        os.system("cls")   
                                         
                    elif choice == "3":
                        # Actualizar especialidad

                        idEspecialidad = input("Ingrese el ID de la especialidad a actualizar: ")
                        nombreEspecialidad = input("Ingrese el nuevo nombre de la especialidad: ")

                        especialidad = especialidadDAO(nombreEspecialidad,idEspecialidad)
                        dto.actualizarEspecialidad(especialidad)
                        print("Especialidad actualizada exitosamente.") 
                                               
                        pass
                        input("Presion enter para volver para contnuar...")
                        os.system("cls")
                                            
                    elif choice == "4":
                        # Listar especialidad
                        
                        especialidades = dto.listarEspecialidad()
                        for especialidad in especialidades:
                            print(f"ID: {especialidad.idEspecialidad}, Nombre: {especialidad.nombreEspecialidad}")                        
                        
                        pass
                        print("")
                        input("Presion enter para volver para contnuar...")
                        os.system("cls")     
                                       
                    elif choice == "5":
                        # Buscar especialidad
                        
                        idEspecialidad = input("Ingrese el ID de la especialidad a buscar: ")
                        especialidad = especialidadDAO(idEspecialidad, '')
                        resultado = dto.buscarEspecialidad(especialidad)

                        if resultado:
                            print(f"ID: {resultado.idEspecialidad}, Nombre: {resultado.nombreEspecialidad}")
                        else:
                            print("La especialidad ingresada no existe.")
                                                
                        pass
                        input("Presion enter para volver para contnuar...")
                        os.system("cls")  
                                          
                    else:
                        print("Opción inválida. Por favor, intenta nuevamente.")  
                        
            elif choice == "5":
                dto = AgendaDTO()
                while True:
                    os.system("cls")
                    agenda_submenu()
                    choice = input("Selecciona una opción: ")
                    os.system("cls")

                    if choice == "0":
                        break
                    elif choice == "1":
                        # Ingresar agenda
                        
                        idAgenda = input("Ingrese el ID de la agenda : ")
                        dia = input("Ingrese el día de la agenda YYYY-MM-DD: ")
                        hora = input("Ingrese la hora de la agenda: ")

                        agenda = agendaDAO(idAgenda, dia, hora)
                        dto.ingresarAgenda(agenda)
                        print("Agenda ingresada exitosamente.")
                        
                        pass
                        input("Presion enter para volver para contnuar...")
                        os.system("cls") 
                                           
                    elif choice == "2":
                        # Eliminar agenda

                        idAgenda = input("Ingrese el ID de la agenda a eliminar: ")
                        agenda = agendaDAO(idAgenda, '', '')

                        if dto.buscarAgenda(agenda):
                            confirmacion = input("¿Está seguro de que desea eliminar la agenda ingresada? (si/no): ")

                            if confirmacion.lower() == "si":
                                dto.eliminarAgenda(agenda)
                                print("La agenda ha sido eliminada exitosamente.")
                            else:
                                print("La eliminación de la agenda ha sido cancelada.")
                        else:
                            print("Error: La agenda ingresada no existe.")                        
                            
                        pass
                        print("")
                        input("Presion enter para volver para contnuar...")
                        os.system("cls") 
                                           
                    elif choice == "3":
                        # Actualizar agenda
                        
                        idAgenda = input("Ingrese el ID de la agenda a actualizar: ")
                        dia = input("Ingrese el nuevo día de la agenda: ")
                        hora = input("Ingrese la nueva hora de la agenda: ")

                        agenda = agendaDAO( dia, hora,idAgenda)
                        dto.actualizarAgenda(agenda)
                        print("Agenda actualizada exitosamente.")
                        
                        pass
                        print("")
                        input("Presion enter para volver para contnuar...")
                        os.system("cls")  
                                          
                    elif choice == "4":
                        # Listar agenda

                        agendas = dto.listarAgenda()
                        for agenda in agendas:
                            print(f"ID: {agenda.idAgenda}, Día: {agenda.dia}, Hora: {agenda.hora}")
                        
                        pass
                        print("")
                        input("Presion enter para volver para contnuar...")
                        os.system("cls")   
                                         
                    elif choice == "5":
                        # Buscar agenda
                        
                        idAgenda = input("Ingrese el ID de la agenda a buscar: ")
                        agenda = agendaDAO(idAgenda, '', '')
                        resultado = dto.buscarAgenda(agenda)

                        if resultado:
                            print(f"ID: {resultado.idAgenda}, Día: {resultado.dia}, Hora: {resultado.hora}")
                        else:
                            print("La agenda ingresada no existe.")
                        
                        pass
                        print("")
                        input("Presion enter para volver para contnuar...")
                        os.system("cls") 
                                           
                    else:
                        print("Opción inválida. Por favor, intenta nuevamente.") 
                        
            elif choice == "6":
                dto = RecetaDTO()
                while True:
                    os.system("cls")
                    receta_submenu()
                    choice = input("Selecciona una opción: ")
                    os.system("cls")

                    if choice == "0":
                        break
                    elif choice == "1":
                        # Ingresar receta
                        
                        idReceta = input("Ingrese el ID de la receta: ")
                        medicamentos = input("Ingrese los medicamentos: ")
                        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
                        rutPaciente = input("Ingrese el RUT del paciente: ")
                        idDoctor = input("Ingrese el ID del doctor: ")

                        receta = recetaDAO(idReceta, medicamentos, fecha, rutPaciente, idDoctor)
                        dto.ingresarReceta(receta)
                        print("Receta ingresada exitosamente.")
                        
                        pass
                        input("Presion enter para volver para contnuar...")
                        os.system("cls") 
                                           
                    elif choice == "2":
                        # Eliminar receta
                        
                        idReceta = input("Ingrese el ID de la receta a eliminar: ")
                        receta = recetaDAO(idReceta, '', '', '', '')

                        if dto.buscarReceta(receta):
                            confirmacion = input("¿Está seguro de que desea eliminar la receta ingresada? (si/no): ")

                            if confirmacion.lower() == "si":
                                dto.eliminarReceta(receta)
                                print("La receta ha sido eliminada exitosamente.")
                            else:
                                print("La eliminación de la receta ha sido cancelada.")
                        else:
                            print("Error: La receta ingresada no existe.")
                            
                        pass
                        input("Presion enter para volver para contnuar...")
                        os.system("cls") 
                                           
                    elif choice == "3":
                        # Actualizar receta
                        
                        idReceta = input("Ingrese el ID de la receta a actualizar: ")
                        medicamentos = input("Ingrese los nuevos medicamentos: ")
                        fecha = input("Ingrese la nueva fecha (YYYY-MM-DD): ")
                        rutPaciente = input("Ingrese el nuevo RUT del paciente: ")
                        idDoctor = input("Ingrese el nuevo ID del doctor: ")

                        receta = recetaDAO(medicamentos, fecha, rutPaciente, idDoctor,idReceta)
                        dto.actualizarReceta(receta)
                        print("Receta actualizada exitosamente.")
                        
                        pass
                        input("Presion enter para volver para contnuar...")
                        os.system("cls") 
                                           
                    elif choice == "4":
                        # Listar receta
                        
                        recetas = dto.listarReceta()
                        for receta in recetas:
                            print(f"ID: {receta.idReceta}, Medicamentos: {receta.medicamentos}, Fecha: {receta.fecha}, RUT Paciente: {receta.rutPaciente}, ID Doctor: {receta.idDoctor}")

                        
                        pass
                        input("Presion enter para volver para contnuar...")
                        os.system("cls")   
                                         
                    elif choice == "5":
                        # Buscar receta
                        
                        idReceta = input("Ingrese el ID de la receta a buscar: ")
                        receta = recetaDAO(idReceta, '', '', '', '')
                        resultado = dto.buscarReceta(receta)

                        if resultado:
                            print(f"ID: {resultado.idReceta}, Medicamentos: {resultado.medicamentos}, Fecha: {resultado.fecha}, RUT Paciente: {resultado.rutPaciente}, ID Doctor: {resultado.idDoctor}")
                        else:
                            print("La receta ingresada no existe.")

                        
                        pass
                        input("Presion enter para volver para contnuar...")
                        os.system("cls")  
                                          
                    else:
                        print("Opción inválida. Por favor, intenta nuevamente.")             

            else:
                print("Opción inválida. Por favor, intenta nuevamente.")

    if __name__ == "__main__":
        main()
    os.system("cls")
print("\n                   **** ||| Gracias por utilizar nuestro sistema ||| ****\n")
from pacienteDAO import pacienteDAO
from pacienteDTO import PacienteDTO

dto = PacienteDTO()

print("prueba\n")
input=("preione enter para continuar....")

#ingresar paciente

insert = pacienteDAO('1111-1','evaristo moya','av vicuña 1400, la florida','9874563','dormir@dormir.cl')
print(dto.ingresarPaciente(insert))

#Eliminar Funcionarios
#delet = pacienteDAO('1111-1','','','','')       
#dto = PacienteDTO()                               
#print(dto.eliminarPaciente(delet))

#actualizar                                                         
#update = pacienteDAO('MAuricio java osho','avenia osho','987456','javasosho@oshos.com','12345678-9') 
#dto = PacienteDTO()                                                          
#print(dto.actualizarPaciente(update))   

#listar pacientes
#print(dto.listarPacientes())

#buscar por rut
#search = pacienteDAO('34567891-3','','','','')       
#dto = PacienteDTO()                             
#print(dto.buscarPaciente(search)) 


from fichaPacienteDAO import FichaPacienteDAO
from fichaPacienteDTO import FichaPacienteDTO

dto = FichaPacienteDTO()

print("prueba\n")


#ingresar 
#insert = FichaPacienteDAO('1767','muerte subita','muerto por moco atravesado','1991-01-02','17675030-8','5','56','25')
#print(dto.ingresarFicha(insert))

#Eliminar 
#delet = FichaPacienteDAO('1767','','','','','','','')       
#dto = FichaPacienteDTO()                               
#print(dto.eliminarFicha(delet))

#actualizar                                                         
update = FichaPacienteDAO('muerte insubita','muerte pokakakakkava','1991-02-01','17675030-8','123','5','56','12') 
dto = FichaPacienteDTO()                                                          
print(dto.actualizarFicha(update))   

#listar pacientes
#print(dto.listarFicha())

#buscar 
#search = FichaPacienteDAO('13','','','','','','','')       
#dto = FichaPacienteDTO()                             
#print(dto.buscarFicha(search)) 


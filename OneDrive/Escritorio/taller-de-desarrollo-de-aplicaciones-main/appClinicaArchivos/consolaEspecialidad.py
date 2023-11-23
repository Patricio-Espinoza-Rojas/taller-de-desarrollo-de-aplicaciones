from especialidadDAO import especialidadDAO
from especialidadDTO import EspecialidadDTO

dto = EspecialidadDTO()

print("prueba\n")

#ingresar 

#insert = especialidadDAO('4','doctor de comadrejas')
#print(dto.ingresarEspecialidad(insert))

#Eliminar 
#delet = especialidadDAO('4','')       
#dto = EspecialidadDTO()                               
#print(dto.eliminarEspecialidad(delet))

#actualizar                                               
          
#update = especialidadDAO('veterinario','12') 
#dto = EspecialidadDTO()                                                          
#print(dto.actualizarEspecialidad(update))   

#listar 
#print(dto.listarEspecialidad())

#buscar 
search = especialidadDAO('12','')       
dto = EspecialidadDTO()                             
print(dto.buscarEspecialidad(search)) 


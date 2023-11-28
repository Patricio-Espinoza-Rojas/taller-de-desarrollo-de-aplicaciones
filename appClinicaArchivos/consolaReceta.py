from recetaDAO import recetaDAO
from recetaDTO import RecetaDTO

dto = RecetaDTO()

print("prueba\n")

#ingresar 
insert = recetaDAO('001','pajacetamol','2023-10-10', '17675030-8','123')
print(dto.ingresarReceta(insert))

#Eliminar 
#delet = recetaDAO('001','','','','')       
#dto = RecetaDTO()                               
#print(dto.eliminarReceta(delet))

#actualizar                                                         
#update = recetaDAO('penedol','2023-10-11','17675030-8','123','001') 
#dto = RecetaDTO()                                                          
#print(dto.actualizarReceta(update))   

#listar 
#print(dto.listarReceta())

#buscar 
#search = recetaDAO('1','','','','')       
#dto = RecetaDTO()                             
#print(dto.buscarReceta(search)) 


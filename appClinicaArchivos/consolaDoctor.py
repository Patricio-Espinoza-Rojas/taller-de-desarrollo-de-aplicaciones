from doctorDAO import doctorDAO
from doctorDTO import DoctorDTO

dto = DoctorDTO()

print("prueba\n")


#ingresar 

#insert = doctorDAO('123','doctor house','diostor','diostor@dios.cl','50','22')
#print(dto.ingresarDoctor(insert))

#Eliminar 
#delet = doctorDAO('123','','','','','')       
#dto = DoctorDTO()                               
#print(dto.eliminarDoctor(delet))

#actualizar                                                         
update = doctorDAO('doctor tin','medico mo','chapati@chapa.cl','50','22','110') 
dto = DoctorDTO()                                                          
print(dto.actualizarDoctor(update))   

#listar 
#print(dto.listarDoctor())

#buscar 
#search = doctorDAO('110','','','','','')       
#dto = DoctorDTO()                             
#print(dto.buscarDoctor(search)) 


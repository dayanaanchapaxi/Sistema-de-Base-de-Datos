#%%importamos modulo y creamos un excel vacio
import pandas as pd
import csv
data_null={}
df_null=pd.DataFrame(data_null)
df_null.to_excel('DatosSinteticos.xlsx', index=False)

from faker import Faker
#%%Cargar y modificar el archivo 
writer=pd.ExcelWriter('DatosSinteticos.xlsx') 

#%%Fake usamos para generar los datos sintéticos de los nombres, de las columnas Nombre Call Center, Usuario, Policia, Accidentado
fake=Faker('es-ES')

##En esta parte del código, establecemos un bucle for b in range(5000), el cual lo usamos para determinar
## la longitud de valores que queremos establecer en cada entidad, en este caso usaremo 5k. 
for b in range(5000):
##Aquí establecemos las variables para generar los datos fake, es decir los datos sinteticos que se generan 
##automáticamente con la declaracion fake.unique.name(), el unique cumple la función de dar datos únicos, 
##es decir que los datos no se repitan, por ejemplo no se repita el mismo nombre como Pablo, dos o más vces
##Por otro lado la parte del .name(), está establecida para establecer nombres, por ende como se ve en el 
#código también existe el .address(), el cual genera direcciones.
    nombresCallCenter = fake.unique.name(),
    nombresUsuario = fake.unique.name()
    UPCPolicia = fake.unique.address() 
    nombresAccidentado = fake.unique.name()
#%%Cargamoms los datos en las celdas de excel en orden, de columnas

data1= {'Operador Call Center':[nombresCallCenter],'Usuario':[nombresUsuario],'UPCPolicia':[UPCPolicia],'Nombre Accidentado':[nombresAccidentado]}
df1 = pd.DataFrame(data1)

#%%Generamos el nombre de la hoja del excel
df1.to_excel(writer,'Hoja 1',index=False)

#%Utilizamos para guardar todos los cambios y datos , y se puedan visualizar en excel
writer.save()
writer.close()

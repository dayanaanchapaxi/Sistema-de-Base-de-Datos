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
nombresCallCenter = [fake.unique.name() for b in range(5000)]
nombresCallCenter


fake=Faker('es-ES')
nombresUsuario = [fake.unique.name() for b in range(5000)]

fake=Faker('es-ES')
nombresPolicia = [fake.unique.name()  for b in range(5000)]
nombresPolicia

fake=Faker('es-ES')
nombresAccidentado = [fake.unique.name() for b in range(5000)]
nombresAccidentado

#%%Cargamoms los datos en las celdas de excel en orden, de columnas

data1= {'Operador Call Center':[nombresCallCenter],'Usuario':[nombresUsuario],'Policia':[nombresPolicia],'Nombre Accidentado':[nombresAccidentado]}
df1 = pd.DataFrame(data1)

#%%Generamos el nombre de la hoja del excel
df1.to_excel(writer,'Hoja 1',index=False)

#%Utilizamos para guardar todos los cambios y datos , y se puedan visualizar en excel
writer.save()
writer.close()
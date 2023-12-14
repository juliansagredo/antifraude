#===========================
# Motor Antifraude 
# Dr. Julián Sagredo 2023 
#===========================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#=====================================================
# Definir partidos como en el archivo de resultados 
#=====================================================
partido1 = 'CC_PVEM_PT_MORENA'
partido2 = 'PAN' 
partido3 = 'PRI'
partido4 = 'PRD' 
partido5 = 'NAEM'
partido6 = 'C_PAN_PRI_PRD_NAEM'
partido7 = 'C_PAN_PRI_PRD'
partido8 = 'C_PAN_PRI_NAEM'
partido9 = 'C_PRD_NAEM'
partido10 = 'C_PRI_NAEM' 
partido11 = 'C_PRI_PRD'
partido12 = 'C_PAN_NAEM'
partido13 = 'C_PAN_PRD_NAEM'
partido14 = 'C_PRI_PRD_NAEM'
partido15 = 'C_PAN_PRI'
partido16 = 'C_PAN_PRD'
personas = "TOTAL_PERSONAS_VOTARON"
tiempo = 'FECHA_HORA_CAPTURA'   

#==================
# Leer los datos 
#==================
datos = pd.read_csv("MEX_GUB_2023.csv", encoding= 'unicode_escape', sep = ',', engine = 'python', header = 4)

#==========================================
# Identificar y quitar líneas con fallas 
#===========================================
lineasmalas = datos[ datos['CONTABILIZADA'] == 0].index
datos.drop( lineasmalas, inplace=True)

#========================
# Convertir a numérico 
#========================
datos = datos._convert(numeric=True) 

#=========================================
# Ordenar datos con el tiempo de captura 
#=========================================
datos_ordenados = datos.sort_values(by=[tiempo])
datos_ordenados.reset_index(inplace=True)
np.array(datos_ordenados)

#=======================
# Total para candidatos
#=======================
total1 = np.array(np.cumsum(datos_ordenados[partido1]))

total2 = np.array(np.cumsum(datos_ordenados[partido2]+datos_ordenados[partido3]+datos_ordenados[partido4]+datos_ordenados[partido5]+datos_ordenados[partido6]+datos_ordenados[partido7]+datos_ordenados[partido8]+datos_ordenados[partido9]+datos_ordenados[partido10]+datos_ordenados[partido11]+datos_ordenados[partido12]+datos_ordenados[partido13]+datos_ordenados[partido14]+datos_ordenados[partido15]+datos_ordenados[partido16]))

total = total1+total2 #np.cumsum(datos_ordenados[personas])

#==============================
# Diferencias entre candidatos
#==============================
diferencia1 = total1 - total2

#==========================
# Evolución del porcentaje 
#==========================
porcentaje1 = 100.0*total1/(total)
porcentaje2 = 100.0*total2/(total)

#=============
#  Gráficas   
#=============
plt.figure(1)
plt.plot(porcentaje1,'purple',porcentaje2,'blue') 
plt.ylabel('Porcentajes durante la captura') 
plt.figure(2)
plt.plot(diferencia1,'red')
plt.ylabel("Diferencia de votos 1o vs 2o")
plt.show()


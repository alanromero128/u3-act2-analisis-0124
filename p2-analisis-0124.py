# importar librerias
import pandas as pd
import numpy as np
print(" Analisis de Detección de Transacciones Fraudulentas Alan Romero NC=0124")
transacciones = {
"Id_Transaccion": ["T001", "T002", "T003", "T003", "T005", "T002"],
"Monto": [15.50, 2500.00, 45.00, 890.00, 90.00, 3400.00],
"Veces": [2,4,6,9,1,7],
"Ubicacion_Inusual": [False, True, False, True, False, True],
"Es_Fraude": [False, True, False, False, False, True]
}
df= pd.DataFrame(transacciones)
print(df)
print("-+-+-+-Agrupar por una sola columna +-+-+-+-+-+")
agrupado =df.groupby('Id_Transaccion')
print(agrupado)
print("-+-+-+-Promedio por Transacciones +-+-+-+-+-+")
# Monto promedio de las transacciones   
print(agrupado['Monto'].mean())
# monto maximo por transacciones
print(agrupado['Monto'].max())

print("-+-+-+-+--+ Alan Romero Segunda parte 0124 -+-+-+-+-+")
print("Agregaciones multiples")
resultado_agregado = agrupado['Monto'].agg(['mean', 'sum', 'max', 'min'])
print("mean-->promedio,sum --> suma")
print("max-->maximo,min --> minimo")
print(resultado_agregado)
print("Agrupacion por varias columnas")
print("Agrea columna al DataFrame")

print("Columna Team -->Equipo ")
df['Equipo'] = ['A','B','A','B','A','B']
agrupado_multiple = df.groupby(['Es_Fraude', 'Equipo'])['Veces'].mean()
print(agrupado_multiple)

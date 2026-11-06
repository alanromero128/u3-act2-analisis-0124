# importar librerias
import pandas as pd
import numpy as np
print(" Analisis de Detección de Transacciones Fraudulentas Alan Romero NC=0124")
transacciones = {
    "Id_Transaccion": ["T001", "T002", "T003", "T003", "T005", "T002"],
    "Monto": [15.50, 2500.00, 45.00, 890.00, 90.00, 3400.00],
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


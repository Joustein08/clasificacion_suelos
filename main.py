from Funciones.Granulometria import *
from Funciones.ValoresEntrada import *
from Funciones.Clasificacion import *

# Masa de cada tamiz
masa_tamiz_4, masa_tamiz_10, masa_tamiz_20, masa_tamiz_30, masa_tamiz_40, masa_tamiz_60, masa_tamiz_140, masa_tamiz_200, masa_fondo, Limite_Liquido, Indice_Plasticidad = Valores()

# Granulometría
print(tablaGranulometria(masa_tamiz_4, masa_tamiz_10, masa_tamiz_20, masa_tamiz_30, masa_tamiz_40, masa_tamiz_60, masa_tamiz_140, masa_tamiz_200, masa_fondo,))

# Tabla granulometría
graficaGranulometria(masa_tamiz_4, masa_tamiz_10, masa_tamiz_20, masa_tamiz_30, masa_tamiz_40, masa_tamiz_60, masa_tamiz_140, masa_tamiz_200, masa_fondo,)

# Clasificación
Clasificación(masa_tamiz_4, masa_tamiz_10, masa_tamiz_20, masa_tamiz_30, masa_tamiz_40, masa_tamiz_60, masa_tamiz_140, masa_tamiz_200, masa_fondo, Limite_Liquido, Indice_Plasticidad)

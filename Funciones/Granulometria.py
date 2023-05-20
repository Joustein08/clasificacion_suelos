# Importación de librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def tablaGranulometria(masa_tamiz_4, masa_tamiz_10, masa_tamiz_20, masa_tamiz_30, masa_tamiz_40, masa_tamiz_60, masa_tamiz_140, masa_tamiz_200, masa_fondo,):
    # Definición de los tamices a utilizar
    TAMICES = pd.Series([
        "# 4", # tamiz # 4
        "# 10", # Tamiz # 10
        "# 20", # Tamiz # 20
        "# 30", # Tamiz # 30
        "# 40", # Tamiz # 40
        "# 60", # Tamiz # 60
        "# 140", # Tamiz # 140
        "# 200", # Tamiz # 200
        "FONDO" # Fondo
    ])

    # Definición de la abertura de los tamices a utilizar [mm]
    ABERTURA = pd.Series([
        4.75, # tamiz # 4
        2, # Tamiz # 10
        0.85, # Tamiz # 20
        0.6, # Tamiz # 30
        0.425, # Tamiz # 40
        0.25, # Tamiz # 60
        0.106, # Tamiz # 140
        0.075, # Tamiz # 200
        np.nan, # Fondo
    ])

    # Definición de la masa retenida para cada tamiz [g]
    RETENIDO = pd.Series([
        masa_tamiz_4, # tamiz # 4
        masa_tamiz_10, # Tamiz # 10
        masa_tamiz_20, # Tamiz # 20
        masa_tamiz_30, # Tamiz # 30
        masa_tamiz_40, # Tamiz # 40
        masa_tamiz_60, # Tamiz # 60
        masa_tamiz_140, # Tamiz # 140
        masa_tamiz_200, # Tamiz # 200
        masa_fondo, # Fondo
    ])

    # Cálculo del porcentaje retenido para cada tamiz
    PORCENTAJE_ret_tamiz_4 = round((masa_tamiz_4/RETENIDO.sum())*100,2) # tamiz # 4
    PORCENTAJE_ret_tamiz_10 = round((masa_tamiz_10/RETENIDO.sum())*100,2) # Tamiz # 10
    PORCENTAJE_ret_tamiz_20 = round((masa_tamiz_20/RETENIDO.sum())*100,2) # Tamiz # 20
    PORCENTAJE_ret_tamiz_30 = round((masa_tamiz_30/RETENIDO.sum())*100,2) # Tamiz # 30
    PORCENTAJE_ret_tamiz_40 = round((masa_tamiz_40/RETENIDO.sum())*100,2) # Tamiz # 40
    PORCENTAJE_ret_tamiz_60 = round((masa_tamiz_60/RETENIDO.sum())*100,2) # Tamiz # 60
    PORCENTAJE_ret_tamiz_140 = round((masa_tamiz_140/RETENIDO.sum())*100,2) # Tamiz # 140
    PORCENTAJE_ret_tamiz_200 = round((masa_tamiz_200/RETENIDO.sum())*100,2) # Tamiz # 200
    PORCENTAJE_ret_fonfo = round((masa_fondo/RETENIDO.sum())*100,2) # Fondo


    # Definición del porcentaje retenido para cada tamiz [%]
    PORCENTAJE_RETENIDO = pd.Series([
        PORCENTAJE_ret_tamiz_4, # tamiz # 4
        PORCENTAJE_ret_tamiz_10, # Tamiz # 10
        PORCENTAJE_ret_tamiz_20, # Tamiz # 20
        PORCENTAJE_ret_tamiz_30, # Tamiz # 30
        PORCENTAJE_ret_tamiz_40, # Tamiz # 40
        PORCENTAJE_ret_tamiz_60, # Tamiz # 60
        PORCENTAJE_ret_tamiz_140, # Tamiz # 140
        PORCENTAJE_ret_tamiz_200, # Tamiz # 200
        PORCENTAJE_ret_fonfo, # Fondo
    ])

    # Definición tabla granulometría
    GRANULOMETRIA =pd.DataFrame({
        "#_TAMIZ" : TAMICES, # Lista de series con los números de los tamices
        "ABERTURA" : ABERTURA, # Lista de series con las aberturas para cada tamiz
        "MASA_RETENIDA" : RETENIDO, # Lista de series con la masa retenida para cada tamiz
        "PORCENTAJE_RETENIDO" : PORCENTAJE_RETENIDO  # Cálculo del porcetaje de masa retenida respecto a la total
    })

    # Agregación de las columnas acumuladas para la masa y el procentaje 
    GRANULOMETRIA["MASA_RETENIDA_ACUMULADA"] = GRANULOMETRIA["MASA_RETENIDA"].cumsum() # Cálculo de la masa acumulada
    GRANULOMETRIA["PORCENTAJE_RETENIDO_ACUMULADO"] = GRANULOMETRIA["PORCENTAJE_RETENIDO"].cumsum() #Cálculo de los porcentajes acumulados

    # Agregación de la columna de los porcentajes pasa para cada tamiz
    GRANULOMETRIA["PORCENTAJE_PASA"] = (100 - GRANULOMETRIA["PORCENTAJE_RETENIDO_ACUMULADO"]) #Cálculo de los porcentajes pasa
    
    return GRANULOMETRIA

def graficaGranulometria(masa_tamiz_4, masa_tamiz_10, masa_tamiz_20, masa_tamiz_30, masa_tamiz_40, masa_tamiz_60, masa_tamiz_140, masa_tamiz_200, masa_fondo,):
    # Definición de los tamices a utilizar
    TAMICES = pd.Series([
        "# 4", # tamiz # 4
        "# 10", # Tamiz # 10
        "# 20", # Tamiz # 20
        "# 30", # Tamiz # 30
        "# 40", # Tamiz # 40
        "# 60", # Tamiz # 60
        "# 140", # Tamiz # 140
        "# 200", # Tamiz # 200
        "FONDO" # Fondo
    ])

    # Definición de la abertura de los tamices a utilizar [mm]
    ABERTURA = pd.Series([
        4.75, # tamiz # 4
        2, # Tamiz # 10
        0.85, # Tamiz # 20
        0.6, # Tamiz # 30
        0.425, # Tamiz # 40
        0.25, # Tamiz # 60
        0.106, # Tamiz # 140
        0.075, # Tamiz # 200
        np.nan, # Fondo
    ])

    # Definición de la masa retenida para cada tamiz [g]
    RETENIDO = pd.Series([
        masa_tamiz_4, # tamiz # 4
        masa_tamiz_10, # Tamiz # 10
        masa_tamiz_20, # Tamiz # 20
        masa_tamiz_30, # Tamiz # 30
        masa_tamiz_40, # Tamiz # 40
        masa_tamiz_60, # Tamiz # 60
        masa_tamiz_140, # Tamiz # 140
        masa_tamiz_200, # Tamiz # 200
        masa_fondo, # Fondo
    ])

    # Cálculo del porcentaje retenido para cada tamiz
    PORCENTAJE_ret_tamiz_4 = round((masa_tamiz_4/RETENIDO.sum())*100,2) # tamiz # 4
    PORCENTAJE_ret_tamiz_10 = round((masa_tamiz_10/RETENIDO.sum())*100,2) # Tamiz # 10
    PORCENTAJE_ret_tamiz_20 = round((masa_tamiz_20/RETENIDO.sum())*100,2) # Tamiz # 20
    PORCENTAJE_ret_tamiz_30 = round((masa_tamiz_30/RETENIDO.sum())*100,2) # Tamiz # 30
    PORCENTAJE_ret_tamiz_40 = round((masa_tamiz_40/RETENIDO.sum())*100,2) # Tamiz # 40
    PORCENTAJE_ret_tamiz_60 = round((masa_tamiz_60/RETENIDO.sum())*100,2) # Tamiz # 60
    PORCENTAJE_ret_tamiz_140 = round((masa_tamiz_140/RETENIDO.sum())*100,2) # Tamiz # 140
    PORCENTAJE_ret_tamiz_200 = round((masa_tamiz_200/RETENIDO.sum())*100,2) # Tamiz # 200
    PORCENTAJE_ret_fonfo = round((masa_fondo/RETENIDO.sum())*100,2) # Fondo


    # Definición del porcentaje retenido para cada tamiz [%]
    PORCENTAJE_RETENIDO = pd.Series([
        PORCENTAJE_ret_tamiz_4, # tamiz # 4
        PORCENTAJE_ret_tamiz_10, # Tamiz # 10
        PORCENTAJE_ret_tamiz_20, # Tamiz # 20
        PORCENTAJE_ret_tamiz_30, # Tamiz # 30
        PORCENTAJE_ret_tamiz_40, # Tamiz # 40
        PORCENTAJE_ret_tamiz_60, # Tamiz # 60
        PORCENTAJE_ret_tamiz_140, # Tamiz # 140
        PORCENTAJE_ret_tamiz_200, # Tamiz # 200
        PORCENTAJE_ret_fonfo, # Fondo
    ])

    # Definición tabla granulometría
    GRANULOMETRIA =pd.DataFrame({
        "#_TAMIZ" : TAMICES, # Lista de series con los números de los tamices
        "ABERTURA" : ABERTURA, # Lista de series con las aberturas para cada tamiz
        "MASA_RETENIDA" : RETENIDO, # Lista de series con la masa retenida para cada tamiz
        "PORCENTAJE_RETENIDO" : PORCENTAJE_RETENIDO  # Cálculo del porcetaje de masa retenida respecto a la total
    })

    # Agregación de las columnas acumuladas para la masa y el procentaje 
    GRANULOMETRIA["MASA_RETENIDA_ACUMULADA"] = GRANULOMETRIA["MASA_RETENIDA"].cumsum() # Cálculo de la masa acumulada
    GRANULOMETRIA["PORCENTAJE_RETENIDO_ACUMULADO"] = GRANULOMETRIA["PORCENTAJE_RETENIDO"].cumsum() #Cálculo de los porcentajes acumulados

    # Agregación de la columna de los porcentajes pasa para cada tamiz
    GRANULOMETRIA["PORCENTAJE_PASA"] = (100 - GRANULOMETRIA["PORCENTAJE_RETENIDO_ACUMULADO"]) #Cálculo de los porcentajes pasa

    # Calculo del diametro de la particula para los porcentajes de 10%, 30% y 60% del pasa tamiz de la granulometría
    interpolacion_granulometria = interp1d(GRANULOMETRIA["PORCENTAJE_PASA"],GRANULOMETRIA["ABERTURA"],kind='linear')
    diametro_10 = interpolacion_granulometria(10)
    diametro_30 = interpolacion_granulometria(30)
    diametro_60 = interpolacion_granulometria(60)

    # Creación de los valores de los ejes para los porcentajes de 10%, 30% y 60% del pasa tamiz de la granulometría
    diametro_10_x = np.array([max(GRANULOMETRIA["ABERTURA"]),diametro_10,diametro_10])
    diametro_10_y = np.array([10,10,0])

    diametro_30_x = np.array([max(GRANULOMETRIA["ABERTURA"]),diametro_30,diametro_30])
    diametro_30_y = np.array([30,30,0])

    diametro_60_x = np.array([max(GRANULOMETRIA["ABERTURA"]),diametro_60,diametro_60])
    diametro_60_y = np.array([60,60,0])

    # Grafica granulometría
    plt.figure(figsize=(12.5, 7.5))
    plt.plot(GRANULOMETRIA["ABERTURA"], GRANULOMETRIA["PORCENTAJE_PASA"],'b-',marker='o',label = "GRANULOMETRÍA SUELO") # Definición caracteristicas curva granulométrica
    plt.plot(diametro_10_x, diametro_10_y,'c--') # Interpolación D_10
    plt.plot(diametro_30_x, diametro_30_y,'c--') # Interpolación D_30
    plt.plot(diametro_60_x, diametro_60_y,'c--') # Interpolación D_60
    plt.xscale("log") # Ajuste de escala logarítmica al eje x
    plt.grid(which='both') # Muestra de la grilla
    plt.yticks(np.arange(0, 110, step=10)) # Ajustes de ticks para el eje y
    plt.xlim(max(GRANULOMETRIA["ABERTURA"]), min(GRANULOMETRIA["ABERTURA"])) # Ajustes de ticks para el eje x

    # Nombre de la gráfica, de los ejes y de los indicativos de los porcentajes 10, 30 y 60
    plt.title("CLASIFICACIÓN SUELOS",fontsize=20) 
    plt.xlabel("TAMAÑO PARTÍCULA",fontsize=10) 
    plt.ylabel("% PASA TAMIZ",fontsize=10)
    plt.annotate('DIAMETRO-10%',(3.9,11),color='c')
    plt.annotate('DIAMETRO-30%',(3.9,31),color='c')
    plt.annotate('DIAMETRO-60%',(3.9,61),color='c')
    plt.legend()
    plt.show()



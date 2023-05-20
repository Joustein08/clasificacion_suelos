# Importación Librerias
from matplotlib.widgets import EllipseSelector
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import numpy as np
import pandas as pd
import matplotlib.colors as mcolors
from scipy.interpolate import interp1d

# Creación de la función carta de plásticidad

def CartaPlasticidad(Limite_Liquido, Indice_Plasticidad):
    # Creación de los valores de los ejes para la línea B
    Linea_B_x = np.array([50,50])
    Linea_B_y = np.array([0,37.8])

    # Creación de los valores de los ejes para la línea U
    Linea_U_x = np.array([8,((60/0.9)+8)])
    Linea_U_y = np.array([0,60])

    # Creación de los valores de los ejes para la línea A
    Linea_A_x = np.array([((4/0.73)+20),100])
    Linea_A_y = np.array([4,(0.73*80)])

    # Creación de los valores para el marco que encierra la gráfica
    Marco_x = np.array([((60/0.9)+8),100,100,8])
    Marco_y = np.array([60,60,0,0])

    # Creación de los valores de la línea inferior para delimitar la zona CL-ML
    CL_x = np.array([((4/0.9)+8),((4/0.73)+20)])
    CL_y = np.array([4,4])

    # Creación de los valores de la línea superior para delimitar la zona CL-ML
    ML_x = np.array([((7/0.9)+8),((7/0.73)+20)])
    ML_y = np.array([7,7])

    # Definición tamaño gráfica y límites por eje
    plt.figure(figsize=(12.5, 7.5))
    plt.xlim(0,100)
    plt.ylim(0,60)

    # Gráfica en punto del suelo a calsificar
    plt.scatter(Limite_Liquido, Indice_Plasticidad, marker='^', s=200, c='saddlebrown', label = "SUELO CLASIFICADO", zorder = 2)

    # Gráficas y etiquetas de las lineas B,U y A
    plt.plot(Linea_B_x, Linea_B_y,'k-')
    plt.plot(Linea_U_x, Linea_U_y,'k--')
    plt.plot(Linea_A_x, Linea_A_y,'k--')
    plt.annotate('LINEA B',(50.5,32.5),color='k',rotation=90)
    plt.annotate('LINEA U',(70.5,55),color='k',rotation=42)
    plt.annotate('LINEA A',(94.5,53),color='k',rotation=36)

    # Gráfica del marco, la sección de CL-ML y la grilla
    plt.plot(Marco_x, Marco_y,'k-')
    plt.plot(CL_x, CL_y,'k-')
    plt.plot(ML_x, ML_y,'k-')
    plt.grid()
    plt.xticks(np.arange(0, 100, step=10))

    # Sombreado por zona con su respectiva etiqueta
    Sombreado_ML_x=[8,50,50,((4/0.73)+20),((4/0.9)+8)]
    Sombreado_ML_y=[0,0,21.9,4,4]
    plt.fill(Sombreado_ML_x,Sombreado_ML_y,'moccasin', zorder = 1)
    plt.annotate('ML',(38,6),color='k',fontsize=15)
    Sombreado_MH_x=[50,100,100,50]
    Sombreado_MH_y=[0,0,(0.73*80),21.9]
    plt.fill(Sombreado_MH_x,Sombreado_MH_y,'orange', zorder = 1)
    plt.annotate('MH',(75,17),color='k',fontsize=15)
    Sombreado_CL_x=[((7/0.9)+8),((7/0.73)+20),50,50]
    Sombreado_CL_y=[7,7,21.9,37.8]
    plt.fill(Sombreado_CL_x,Sombreado_CL_y,'lemonchiffon', zorder = 1)
    plt.annotate('CL',(35,17),color='k',fontsize=15)
    Sombreado_CH_x=[50,100,100,((60/0.9)+8),50]
    Sombreado_CH_y=[21.9,(0.73*80),60,60,37.8]
    plt.fill(Sombreado_CH_x,Sombreado_CH_y,'gold', zorder = 1)
    plt.annotate('CH',(65,42),color='k',fontsize=15)
    Sombreado_CL_ML_x=[((4/0.9)+8),((4/0.73)+20),((7/0.73)+20),((7/0.9)+8)]
    Sombreado_CL_ML_y=[4,4,7,7]
    plt.fill(Sombreado_CL_ML_x,Sombreado_CL_ML_y,'khaki', zorder = 1)
    plt.annotate('CL-ML',(17.5,4.5),color='k',fontsize=15)

    # Nombre de la gráfica y de los ejes
    plt.title("CLASIFICACIÓN SUELOS",fontsize=20) 
    plt.xlabel("LÍMITE LÍQUIDO",fontsize=10) 
    plt.ylabel("ÍNDICE DE PLASTICIDAD",fontsize=10) 
    plt.legend()
    plt.show()

# Importación de librerias
import pandas as pd

# Importación de funciones de otros archivos
from Funciones.Granulometria import *
from Funciones.CartaPlasticidad import *

# Funciones para los cálculos de las líneas
def Linea_U(X):
  return (0.9*(X-8)) 
def Linea_A(X):
  return (0.73*(X-20))

def Clasificación(masa_tamiz_4, masa_tamiz_10, masa_tamiz_20, masa_tamiz_30, masa_tamiz_40, masa_tamiz_60, masa_tamiz_140, masa_tamiz_200, masa_fondo, Limite_Liquido, Indice_Plasticidad):
# Granulometria
    GRANULOMETRIA = pd.DataFrame(tablaGranulometria(masa_tamiz_4, masa_tamiz_10, masa_tamiz_20, masa_tamiz_30, masa_tamiz_40, masa_tamiz_60, masa_tamiz_140, masa_tamiz_200, masa_fondo,))

    # CLASIFICACIÓN SUELO
    if GRANULOMETRIA.iloc[7,6] < 50:
        
        print("El suelo es grueso")
        print("-------------------------------------------------------")
        
        # Calculo del diametro de la particula para los porcentajes de 10%, 30% y 60% del pasa tamiz de la granulometría
        interpolacion_granulometria = interp1d(GRANULOMETRIA["PORCENTAJE_PASA"],GRANULOMETRIA["ABERTURA"],kind='linear')
        diametro_10 = interpolacion_granulometria(10)
        diametro_30 = interpolacion_granulometria(30)
        diametro_60 = interpolacion_granulometria(60)

        #Calculo de coeficiente de uniformidad (Cu)
        Cu = diametro_60/diametro_10

        #Calculo de coeficiente de curvatura (Cc) 
        Cc = (diametro_30**2)/(diametro_60*diametro_10)
        
        # Clasificación del suelo grueso
        if GRANULOMETRIA.iloc[0,6]<50:
            if GRANULOMETRIA.iloc[7,6]<=5:
                if Cu >= 4 and Cc <= 3:
                    print("El suelo es una grava bien graduada (GW)")
                elif Cu < 4 and Cc <= 3:
                    print("El suelo es una grava pobremente graduada (GP)")
                else:
                    print("ERROR")
            elif 5<GRANULOMETRIA.iloc[7,6]<=12:
                if Cu >= 4 and Cc <= 3 and Linea_A(Limite_Liquido)>Indice_Plasticidad:
                    print("El suelo es una grava limosa bien graduada(GW-GM)")
                elif Cu < 4 and Cc <= 3 and Linea_A(Limite_Liquido)>Indice_Plasticidad:
                    print("El suelo es una grava limosa pobremente graduada(GP-GM)")
                elif Cu >= 4 and Cc <= 3 and Linea_A(Limite_Liquido)<=Indice_Plasticidad<Linea_U(Limite_Liquido):
                    print("El suelo es una grava arcillosa bien graduada(GW-GC)")
                elif Cu < 4 and Cc <= 3 and Linea_A(Limite_Liquido)<=Indice_Plasticidad<Linea_U(Limite_Liquido):
                    print("El suelo es una grava arcillosa pobremente graduada(GP-GC)")
                else:
                    print("ERROR")
            else:
                if Linea_A(Limite_Liquido)>Indice_Plasticidad:
                    print("El suelo es una grava limosa (GM)")
                elif Linea_A(Limite_Liquido)<=Indice_Plasticidad<Linea_U(Limite_Liquido):
                    print("El suelo es una grava arcillosa (GC)")
                else:
                    print("ERROR")
        else:
            if GRANULOMETRIA.iloc[7,6]<=5:
                if Cu >= 6 and Cc <= 3:
                    print("El suelo es una arena bien graduada (SW)")
                elif Cu < 6 and Cc <= 3:
                    print("El suelo es una arena pobremente graduada (SP)")
                else:
                    print("ERROR")
            elif 5<GRANULOMETRIA.iloc[7,6]<=12:
                if Cu >= 6 and Cc <= 3 and Linea_A(Limite_Liquido)>Indice_Plasticidad:
                    print("El suelo es una arena limosa bien graduada(SW-SM)")
                elif Cu < 6 and Cc <= 3 and Linea_A(Limite_Liquido)>Indice_Plasticidad:
                    print("El suelo es una arena limosa pobremente graduada(SP-SM)")
                elif Cu >= 6 and Cc <= 3 and Linea_A(Limite_Liquido)<=Indice_Plasticidad<Linea_U(Limite_Liquido):
                    print("El suelo es una arena arcillosa bien graduada(SW-SC)")
                elif Cu < 6 and Cc <= 3 and Linea_A(Limite_Liquido)<=Indice_Plasticidad<Linea_U(Limite_Liquido):
                    print("El suelo es una arena arcillosa pobremente graduada(SP-SC)")
                else:
                    print("ERROR")
            else:
                if Linea_A(Limite_Liquido)>Indice_Plasticidad:
                    print("El suelo es una arena limosa (SM)")
                elif Linea_A(Limite_Liquido)<=Indice_Plasticidad<Linea_U(Limite_Liquido):
                    print("El suelo es una arena arcillosa (SC)")
                else:
                    print("ERROR")
    else:
        print("El suelo es fino")
        print("-------------------------------------------------------")
        CartaPlasticidad(Limite_Liquido, Indice_Plasticidad)
        # Clasificación del suelo por carta de plasticidad
        if 8<=Limite_Liquido<((4/0.9)+8):
            if 0<=Indice_Plasticidad<Linea_U(Limite_Liquido):
                print("El suelo es un Limo de de Baja Plasticidad (ML)")
            else:
                print("ERROR")
        elif ((4/0.9)+8)<=Limite_Liquido<((7/0.9)+8):
            if 0<=Indice_Plasticidad<4:
                print("El suelo es un Limo de de Baja Plasticidad (ML)")
            elif 4<=Indice_Plasticidad<Linea_U(Limite_Liquido):
                print("El suelo es una arcilla limosa de baja plasticidad(CL-ML)")
            else:
                print("ERROR")
        elif ((7/0.9)+8)<=Limite_Liquido<((4/0.73)+20):
            if 0<=Indice_Plasticidad<4:
                print("El suelo es un Limo de de Baja Plasticidad (ML)")
            elif 4<=Indice_Plasticidad<7:
                print("El suelo es una arcilla limosa de baja plasticidad(CL-ML)")
            elif 7<=Indice_Plasticidad<Linea_U(Limite_Liquido):
                print("El suelo es una Arcilla de Baja Plasticidad (CL)")
            else :
                print("ERROR")
        elif ((4/0.73)+20)<=Limite_Liquido<((7/0.73)+20):
            if 0<=Indice_Plasticidad<Linea_A(Limite_Liquido):
                print("El suelo es un Limo de de Baja Plasticidad (ML)")
            elif Linea_A(Limite_Liquido)<=Indice_Plasticidad<7:
                print("El suelo es una arcilla limosa de baja plasticidad(CL-ML)")
            elif 7<=Indice_Plasticidad<Linea_U(Limite_Liquido):
                print("El suelo es una Arcilla de Baja Plasticidad (CL)")
            else :
                print("ERROR")
        elif ((7/0.73)+20)<=Limite_Liquido<50:
            if 0<=Indice_Plasticidad<Linea_A(Limite_Liquido):
                print("El suelo es un Limo de de Baja Plasticidad (ML)")
            elif Linea_A(Limite_Liquido)<=Indice_Plasticidad<Linea_U(Limite_Liquido):
                print("El suelo es una Arcilla de Baja Plasticidad (CL)")
            else:
                print("ERROR")
        else:
            if 0<=Indice_Plasticidad<Linea_A(Limite_Liquido):
                print("El suelo es un Limo de de Alta Plasticidad (MH)")
            elif Linea_A(Limite_Liquido)<=Indice_Plasticidad<Linea_U(Limite_Liquido):
                print("El suelo es una Arcilla de Alta Plasticidad (CH)")
            else:
                print("ERROR")


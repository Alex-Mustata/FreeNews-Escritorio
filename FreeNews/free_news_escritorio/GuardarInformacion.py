import os
import pandas as pd # type: ignore
import FreeNews as fn
import datetime

#Crearemos un archivo .csv para guardar la siguiente información:
#ruta + titular, enlace, portal de noticias, fecha de acción realizada.

class GuardarInformacion:
    
    

    def crear_dataframe(titular, enlace, portal):
        
        if not os.path.exists('..\\free_news_escritorio\\informacion.csv'):
            with open('..\\free_news_escritorio\\informacion.csv', 'w', encoding='utf-8'):
                pass

        columnas = {
        'TITULAR' : titular,
        'ENLACE' : enlace,
        'PORTAL' : portal,
        'FECHA' : [datetime.datetime.now()]
        }

        datos = pd.DataFrame(columnas)
        
        if os.path.getsize('..\\free_news_escritorio\\informacion.csv') == 0: 
            #getsize recupera la cantidad de bytes de un archivo
            #si es 0 significa que se encuentra vacío
            datos.to_csv('..\\free_news_escritorio\\informacion.csv',index=False)
        else:
            datos.to_csv('..\\free_news_escritorio\\informacion.csv',mode='a',index=False, header = False)
        

    def leer_dataframe():
        if not os.path.exists('..\\free_news_escritorio\\informacion.csv'):
            return 'csv inexistente'
        if os.path.getsize('..\\free_news_escritorio\\informacion.csv') == 0: 
            return 'csv vacío'
        datos = pd.read_csv('..\\free_news_escritorio\\informacion.csv')
        return datos



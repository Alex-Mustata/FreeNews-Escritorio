import urllib.request
import json
import os
import GuardarInformacion # type: ignore
from  bs4 import BeautifulSoup # type: ignore

class UrlError(ValueError):
    pass

class LeerNoticias:
    
    portales_csv = []
    soup = ''
    noticia = ''
    url = ''

    def crear_carpeta():
        if not os.path.isdir('news'):
            os.mkdir('news')

    def desencriptar_noticia(url_java_python):
        LeerNoticias.crear_carpeta()
        LeerNoticias.url = url_java_python
        req = urllib.request.Request(LeerNoticias.url)
        req.add_header('user-agent', 'Mozilla/5.0')

        with urllib.request.urlopen(req) as response:
            contenido = response.read() 
            LeerNoticias.noticia = contenido.decode('utf-8') 
                
        LeerNoticias.soup = BeautifulSoup(LeerNoticias.noticia, 'html.parser')

        texto = f'{LeerNoticias.soup.h1.text}.txt'
        
        #Estos carácteres causan problemas así que los eliminamos
        if '\n' in texto:
            texto = texto.replace('\n', '')
        if '|' in texto:
            texto = texto.replace('|', '')
        if ':' in texto:
            texto = texto.replace(':', '')
        if '?' in texto:
            texto = texto.replace('?', '')
        
        texto = texto.strip(" ")

        return texto #Devuelve titular


    def el_pais(self, url_java_python):
            try:
                
                noticia = LeerNoticias.desencriptar_noticia(url_java_python)

                if not 'elpais' in LeerNoticias.url:
                    raise UrlError
                else:

                    #Añadir .txt con el titular en la carpeta titulares
                    with open(f"..\\free_news_escritorio\\titulares.txt", 'a+', encoding='utf-8') as f:
                                f.write(f'{noticia}\n')

                    LeerNoticias.portales_csv.append('EL PAIS') 
                #Se consigue todos los scripts de ese tipo, ya que ahí se encuentra la noticia
                data = LeerNoticias.soup.find_all('script', type="application/ld+json")
                print(noticia)
                #iteramos en cada script hasta encontrar el indicado con la noticia
                for i in data:
                    jason = json.loads(i.text) #Como los scripts son tipo json, usamos json.loads para convertirlos en texto y leerlos
                    if isinstance(jason, dict) and "articleBody" in jason.keys(): #comprobamos si el json leido es dict y si contiene articleBody, la noticia, la escribimos
                        with open(f"..\\free_news_escritorio\\news\\{noticia}", 'a', encoding='utf-8') as f:
                            f.write(jason["articleBody"])
            

            except UrlError:
                print('La URL no es de El Pais')
            except urllib.error.URLError:
                print('Internet no disponible')
            else:
                print('Operacion realizada con exito')
                GuardarInformacion.GuardarInformacion.crear_dataframe(noticia, LeerNoticias.url, LeerNoticias.portales_csv[-1])
            
    def diario_sur(self, url_java_python):
        try:
            
            noticia = LeerNoticias.desencriptar_noticia(url_java_python)

            if 'diariosur' not in LeerNoticias.url:
                raise UrlError
            else:
                    #Añadir .txt con el titular en la carpeta titulares
                    with open(f"..\\free_news_escritorio\\titulares.txt", 'a+', encoding='utf-8') as f:
                                f.write(f'{noticia}\n')

                    LeerNoticias.portales_csv.append('DIARIO SUR')
            parrafos = LeerNoticias.soup.find_all("p", class_ = "v-p") 
            #busca los parrafos de la clase v-p, que contiene la noticia y algúna cosa inecesaria que eliminaremos después
            contador = 0


            with open(f"..\\free_news_escritorio\\news\\{noticia}", 'a', encoding='utf-8') as f:
                for i in parrafos:
                    if contador > 11:
                        f.write(f'{i.get_text()}\n')
                    contador += 1

        except UrlError:
            print('La URL no es del Diario Sur')
        except ValueError:
            print('URL invalida')
        except urllib.error.URLError:
            print('Internet no disponible')
        else:
            GuardarInformacion.GuardarInformacion.crear_dataframe(noticia, LeerNoticias.url, LeerNoticias.portales_csv[-1])
            print('Operacion realizada con exito')

    def el_diario(self, url_java_python):
        try: 

            noticia = LeerNoticias.desencriptar_noticia(url_java_python)

            if 'eldiario' not in LeerNoticias.url:
                raise UrlError
            else:
                    #Añadir .txt con el titular en la carpeta titulares
                    with open(f"..\\free_news_escritorio\\titulares.txt", 'a+', encoding='utf-8') as f:
                                f.write(f'{noticia}\n')

                    LeerNoticias.portales_csv.append('EL DIARIO') 
            parrafos = LeerNoticias.soup.find_all("p", class_="article-text")

            with open(f"..\\free_news_escritorio\\news\\{noticia}", 'a', encoding='utf-8') as f:
                for i in parrafos:
                    x = i.get_text().lstrip()
                    f.write(x)

        except UrlError:
            print('La URL no es del El Diario')
        except ValueError:
            print('URL invalida')
        except urllib.error.URLError:
            print('Internet no disponible')
        else:
            GuardarInformacion.GuardarInformacion.crear_dataframe(noticia, LeerNoticias.url, LeerNoticias.portales_csv[-1])
            print('Operacion realizada con exito')

    def abc(self, url_java_python):
        try:
            noticia = LeerNoticias.desencriptar_noticia(url_java_python)

            if 'abc' not in LeerNoticias.url:
                raise UrlError
            else:
                #Añadir .txt con el titular en la carpeta titulares
                    with open(f"..\\free_news_escritorio\\titulares.txt", 'a+', encoding='utf-8') as f:
                                f.write(f'{noticia}\n')

                    LeerNoticias.portales_csv.append('ABC') 

            parrafos = LeerNoticias.soup.find_all("p", class_ = "v-d-p") 
            
            
            with open(f"..\\free_news_escritorio\\news\\{noticia}", 'a', encoding='utf-8') as f:
                for i in parrafos:
                    f.write(i.get_text())
        
        except UrlError:
            print('La URL no es del ABC')
        except ValueError:
            print('URL invalida')
        except urllib.error.URLError:
            print('Internet no disponible')
        else:
            GuardarInformacion.GuardarInformacion.crear_dataframe(noticia, LeerNoticias.url, LeerNoticias.portales_csv[-1])
            print('Operacion realizada con exito')

    
    def diario_vasco(self, url_java_python): #Es el mismo código que diario sur
        try:
            
            noticia = LeerNoticias.desencriptar_noticia(url_java_python)

            if 'diariovasco' not in LeerNoticias.url:
                raise UrlError
            else:
                #Añadir .txt con el titular en la carpeta titulares
                with open(f"..\\free_news_escritorio\\titulares.txt", 'a+', encoding='utf-8') as f:
                            f.write(f'{noticia}\n')

                LeerNoticias.portales_csv.append('DIARIO VASCO') 
            parrafos = LeerNoticias.soup.find_all("p", class_ = "v-p") 
            #busca los parrafos de la clase v-p, que contiene la noticia y algúna cosa inecesaria que eliminaremos después
            contador = 0


            with open(f"..\\free_news_escritorio\\news\\{noticia}", 'a', encoding='utf-8') as f:
                for i in parrafos:
                    if contador > 11:
                        f.write(f'{i.get_text()}\n')
                    contador += 1

        except UrlError:
                print('La URL no es del Diario Sur')
        except ValueError:
            print('URL invalida')
        except urllib.error.URLError:
            print('Internet no disponible')
        else:
            GuardarInformacion.GuardarInformacion.crear_dataframe(noticia, LeerNoticias.url, LeerNoticias.portales_csv[-1])
            print('Operacion realizada con exito')

if __name__ == '__main__':
    objeto = LeerNoticias()
    lista_contenido = []

    with open('..\\free_news_escritorio\\java_python.txt', 'r', encoding='utf-8-sig') as java_python:
        
        for linea in java_python:
            lista_contenido.append(linea.strip())
    
    if lista_contenido[0] == 'elpais':
        objeto.el_pais( lista_contenido[1] )
    elif lista_contenido[0] == 'diariosur':
        objeto.diario_sur( lista_contenido[1] )
    elif lista_contenido[0] == 'eldiario':
        objeto.el_diario( lista_contenido[1] )
    elif lista_contenido[0] == 'abc':
        objeto.abc( lista_contenido[1] )
    elif lista_contenido[0] == 'diariovasco':
        objeto.diario_vasco( lista_contenido[1] )
    
    
        
        
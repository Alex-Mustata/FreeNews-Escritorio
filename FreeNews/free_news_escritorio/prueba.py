from urllib.request import Request, urlopen

req = Request(
    url=input('inserte enlace:'), 
    headers={'User-Agent': 'Mozilla/5.0'}
)
webpage = urlopen(req).read()
noticia= webpage.decode('utf-8')

print(noticia)
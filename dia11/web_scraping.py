from bs4 import BeautifulSoup
import requests
import urllib3

# Desactivamos el warning de SSL porque confiamos en el sitio
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

resultado = requests.get("https://fede-garay.vercel.app/", verify=False)
sopa = BeautifulSoup(resultado.text, "lxml") 

for titulo in sopa.select("#videos h3"):
    print(titulo.get_text())

for link in sopa.select("#videos a"):
    print(link.get("href"))
    
imagenes = sopa.select("img")[0]  # Seleccionamos las primeras 5 imágenes
print(imagenes["src"])

url_imagen = "https://fede-garay.vercel.app".rstrip("/") + imagenes["src"]

respuesta_imagen = requests.get(url_imagen, verify=False).content

foto= open("foto.jpg", "wb")
foto.write(respuesta_imagen)   
foto.close()


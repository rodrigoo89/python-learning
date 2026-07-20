from bs4 import BeautifulSoup
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



url = "https://books.toscrape.com/catalogue/page-1.html"
# verify=False: la red corporativa intercepta HTTPS con un certificado propio
# que Python no reconoce. Solo para practicar en este entorno.

def recorrer_paginas():
    libros_bien_calificados = []
    for pagina in range(1, 2):  # 50 páginas
        print(f"Procesando página {pagina}...")
        url_pagina = f"https://books.toscrape.com/catalogue/page-{pagina}.html"
        response = requests.get(url_pagina, verify=False)
        soup = BeautifulSoup(response.text, "lxml")

       

        for libro in soup.find_all("article", class_="product_pod"):
            rating = libro.find("p", class_="star-rating")
            estrellas = rating["class"] #rating es un atributo de la etiqueta p, y su valor es una lista de clases. La primera clase es "star-rating" y la segunda clase indica el número de estrellas (por ejemplo, "One", "Two", "Three", "Four", "Five").

            if "Four" in estrellas or "Five" in estrellas:
                titulo = libro.h3.a["title"]
                libros_bien_calificados.append(titulo)

    return libros_bien_calificados
  

for titulo in recorrer_paginas():
    print(titulo)
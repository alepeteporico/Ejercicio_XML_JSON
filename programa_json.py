import json
with open("movies.json") as fichero:
    datos=json.load(fichero)

while True:
    print("================================================================================")
    print("1.Listar el título, año y duración de todas las películas.")
    print("2.Mostrar los títulos de las películas y el número de actores/actrices que tiene cada una.")
    print("3.Mostrar las películas que contengan en la sinopsis dos palabras dadas.")
    print("4.Mostrar las películas en las que ha trabajado un actor dado.")
    print("5.Mostrar el título y la url del póster de las tres películas con una media de puntuaciones más alta y lanzadas entre dos fechas dadas.")
    print("6.Salir")
    print("================================================================================")
    elec=int(input("Elige una opción: "))
    print("")

    if elec==6:
        break
    
    elif elec==1:
        lista_peliculas=[]
        lista_año=[]

        lista_peliculas=(datos.get("title"))
        lista_año=(datos.get("year"))

        for pelicula in lista_peliculas:
            print("-",pelicula)
            for año in lista_año:
                print("-",año)
                print("--------------")
        
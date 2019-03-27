from lxml import etree
doc=etree.parse('radares.xml')

while True:
    print("================================================================================")
    print("1.Mostrar el nombre de las provincias de las que tenemos información sobre radares.")
    print("2.Mostrar la cantidad de radares de los que tenemos información.")
    print("3.Pedir por teclado una provincia y mostrar el nombre de las carreteras que tiene y la cantidad de radares.")
    print("4.Pedir por teclado una carretera, muestra las provincias por la que pasa y sus respectivos radares.")
    print("5.Pedir por teclado una carretera, cuenta los radares que tiene y muestra las coordenadas de los radares.(Se puede obtener la URL de OpenStraeetMap para ver donde está el radar).")
    print("6.Salir")
    print("================================================================================")
    elec=int(input("Elige una opción: "))
    print("")

    if elec==6:
        break

    elif elec==1:
        lista=doc.xpath("/RAIZ/PROVINCIA/NOMBRE/text()")
    
        for provincia in lista:
            print("-",provincia)

        print("------------------------------")
        intro=input("Pulsa enter para continuar")
        print("")
    
    elif elec==2:
        lista=doc.xpath("/RAIZ/PROVINCIA/CARRETERA/RADAR")
        print(len(lista),"radares hay")

        print("------------------------------")
        intro=input("Pulsa enter para continuar")
        print("")
    
    elif elec==3:
        provincia=input("Dime una provincia: ")
        
        validacion=doc.xpath("/RAIZ/PROVINCIA/NOMBRE/text()")

        if provincia in validacion:
            lista_carreteras=doc.xpath("/RAIZ/PROVINCIA[NOMBRE='{}']/CARRETERA/DENOMINACION/text()".format(provincia))
            lista_radar=doc.xpath("/RAIZ/PROVINCIA[NOMBRE='{}']/CARRETERA/RADAR".format(provincia))
            print("LAS CARRETERAS SON:")
            for carretera in lista_carreteras:
                print("-",carretera)
            
            print("Hay",len(lista_radar), "radares")
        else:
            print("LA PROVINCIA INTRODUCIDA NO EXISTE")
        
        print("------------------------------")
        intro=input("Pulsa enter para continuar")
        print("")

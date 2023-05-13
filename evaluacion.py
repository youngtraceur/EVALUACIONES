opcion = ""
ccestrellan = 0
cchamps= 0
cmeganium = 0
cdonkie = 0
cestrellan = 500
champs = 4000
meganium = 2500
donkie = 2000
ventatotal = 0
precio = 0



while opcion != "5":
    print("Bienvenido/a a helados wena wena")
    print("A continuación se muestra la lista de opciones disponibles:")
    print("1. Cestrellan - $500")
    print("2. Champs - $4,000")
    print("3. Meganium - $2,500")
    print("4. Donkie - $2,000")
    print("5. Salir")

    opcion = input("Ingrese la opcion de helado que desea: ")
    if opcion not in ("1", "2", "3","4","5", "6"):
        print("**********opcion no valida peaso de perguetano klo**********")


    elif opcion == "1":
        ccestrellan += 1
        edad = int(input("Ingrese la edad del cliente: "))
        if edad < 18 or edad > 65:
            preciodescuento = cestrellan * 0.9
            print("descuento del 10% valido sobre el precio del producto por: ",preciodescuento)
            precio +=preciodescuento
        else:
            print("edad para descuento no aplica basura, total es: ",cestrellan)
            print("Cestrellan agregado al carro.")
            precio +=500

    elif opcion == "2":
        cchamps += 1
        edad = int(input("Ingrese la edad del cliente: "))
        if edad < 18 or edad > 65:
            preciodescuento = champs * 0.9
            print("descuento del 10% valido sobre el precio del producto por: ",preciodescuento)
            precio +=preciodescuento
        else:
            print("edad para descuento no aplica basura, total es: ",champs)
            print("Champs agregado al carro.")
            precio +=4000

    elif opcion == "3":
        cmeganium += 1
        edad = int(input("Ingrese la edad del cliente: "))
        if edad < 18 or edad > 65:
            preciodescuento = meganium * 0.9
            print("descuento del 10% valido sobre el precio del producto por: ",preciodescuento)
            precio +=preciodescuento
        else:
            print("edad para descuento no aplica basura, total es: ",meganium)
            print("Meganium agregado al carro.")
            precio +=2500 
    elif opcion == "4":
        cdonkie += 1
        edad = int(input("Ingrese la edad del cliente: "))
        if edad < 18 or edad > 65:
            preciodescuento = donkie * 0.9
            print("descuento del 10% valido sobre el precio del producto por: ",preciodescuento)
            precio +=preciodescuento
        else:
            print("edad para descuento no aplica basura, total es: ",donkie)
            print("donkie agregado al carro.")
            precio +=2000

    elif opcion == "5":
        print("Reporte de productos vendidos:")
        print("- Cestrellan: {} unidades vendidas".format(ccestrellan))
        print("- Champs: {} unidades vendidas".format(cchamps))
        print("- Meganium: {} unidades vendidas".format(cmeganium))
        print("- Donkie: {} unidades vendidas".format(cdonkie))
        print("- Total de {} helados vendidos".format(ccestrellan+cchamps+cmeganium+cdonkie))
        print("Ventas totales: ${}".format(precio))
        break

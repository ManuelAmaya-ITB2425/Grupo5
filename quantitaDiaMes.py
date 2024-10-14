try:
    mes = int(input("Mes? "))

    if mes >= 1 and mes <= 12:
        if mes in(12,10,8,7,5,1):
            print("Este mes tiene 31 dias")
        elif mes  in(11,9,6,4):
            print("Este mes tiene 30 dias")
        else:
            print("28 o 29")
            #TODO any de traspas?
    else:
        print("Mes incorrecto")
except ValueError:
    print("Por favor pon los meses en numeros")
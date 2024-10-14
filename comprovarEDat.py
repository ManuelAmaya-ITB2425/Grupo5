from datetime import datetime

dia = int(input("Dia de naixement? "))
mes = int(input("Mes de naixement? "))
any = int(input("Any de naixement? "))
anyActual = datetime.now().year

if any <= anyActual:
    if mes >= 1 and mes <= 12:
        if dia >= 1 and dia <= 31:
            #TODO comprovar año de traspaso
            if anyActual - any >= 16 and anyActual - any <= 65:
                print("Puedes trabajar")
        else:
            print("Dia erroneo")
    else:
        print("Mes erroneo")
else:
    print("Año erroneo")

print("Fin del programa")


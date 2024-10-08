#Obtenir les dadaes
from datetime import datetime

ahora= datetime.now().year

dia=int(input("Dia de naixement?"))
mes=int(input("Mes de naixement?"))
any=int(input("Any de naixement?"))

#Validar les dades
if dia > 31:
    print("Dia incorrecte")
if mes > 12:
    print("Mes incorrecte")
if any > ahora:
    print("Any incorrecte")


#Procesa les dades
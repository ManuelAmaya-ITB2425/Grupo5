import xml.etree.ElementTree as ET #ElementTree es una biblioteca en Python que permet analitzar i crear dades XML
import json
from datetime import datetime


#Para analizar, cargar y obtener el nodo raíz
archivoXML = ET.parse("incidenciasOK.xml")
raiz = archivoXML.getroot()


#Inicia las variables para contar las variables, tanto las válidas como las que no
contadorTotal = 0
contadorBuenas = 0
contadorMalas = 0
incidencias = []

#Índica las fechas límites (de 1980 a la fecha actual)
fechaLimiteInferior = datetime(1980, 1, 1)
fechaActual = datetime.now()

#Busca cada entrada del elemento row del archivo y extraemos los valores dentro de este, especificando la incidencia
for row in raiz.findall('row'):
    marcaTemps = row.find('Marca_de_temps').text
    adreça = row.find('Adreça_electrònica').text
    informacio = row.find('Informació_relativa_sobre_la_protecció_de_dades_en_compliment_del_Reglament_General_de_Protecció_de_Dades__Reglament_UE_2016_679_del_Parlament_Europeu_i_del_Consell__de_27_d_abril_de_2016_').text
    nomCognom = row.find('NOM_i_COGNOMS').text
    dataIncidencia = row.find('DATA_DE_LA_INCIDÈNCIA').text
    tipusIncidencia = row.find('TIPUS_INCIDÈNCIA').text
    equipsAfectats = row.find('EQUIPS_i_o_SERVEIS_AFECTATS').text
    propostaSolucio = row.find('DESCRIPCIÓ____PROPOSTA_DE_SOLUCIÓ').text
    nivelUrgencia = row.find('NIVELL_URGÈNCIA_DE_SOLUCIÓ').text

    #Verifica si tiene un valor válido
    if dataIncidencia is not None:
        try:
            #Convierte la fecha de la incidencia en un objeto datatime
            dataIncidenciaDT = datetime.strptime(dataIncidencia, "%d/%m/%Y")
        except ValueError:
            #Si hay un error en el formato de la fecha, se considerará incorrecta
            contadorMalas += 1
            print(f"Error de format de data: {dataIncidencia} per {nomCognom}")
            continue
        #Verifica si la fecha está dentro del rango especificado
        if fechaLimiteInferior <= dataIncidenciaDT <= fechaActual:
            contadorBuenas += 1
            valid = True
        else:
            contadorMalas += 1
            valid = False

    #Muestra la información de las incidencias
    print(f'Marca_de_Temps:\033[0;31;40m'f'{marcaTemps}\033[0;0m   '
          f'Adreça_electrònica:\033[0;32;40m'f'{adreça}\033[0;0m   '
          f'Informació_relativa_sobre_la_protecció_de_dades_en_compliment_del_Reglament_General_de_Protecció_de_Dades__Reglament_UE_2016_679_del_Parlament_Europeu_i_del_Consell__de_27_d_abril_de_2016_:\033[1;3;4;33;40m'f'{informacio}\033[0;0m   '
          f'NOM_i_COGNOMS:\033[0;34;40m'f'{nomCognom}\033[0;0m   '
          f'DATA_DE_LA_INCIDÈNCIA:\033[0;35;40m'f'{dataIncidencia}\033[0;0m   '
          f'TIPUS_INCIDÈNCIA:\033[0;36;40m'f'{tipusIncidencia}\033[0;0m   '
          f'EQUIPS_i_o_SERVEIS_AFECTATS:\033[0;37;40m'f'{equipsAfectats}\033[0;0m   '
          f'DESCRIPCIÓ____PROPOSTA_DE_SOLUCIÓ:\033[0;38;40m'f'{propostaSolucio}\033[0;0m   '
          f'NIVELL_URGÈNCIA_DE_SOLUCIÓ:\033[0;30;47m'f'{nivelUrgencia}\033[0;0m   ')

    # Guardar la incidencia en la lista
    incidencia = {
        "Marca_de_Temps": marcaTemps,
        "Adreça_electrònica": adreça,
        "Informació": informacio,
        "Nom_i_Cognoms": nomCognom,
        "Data_de_la_Incidència": dataIncidencia,
        "Tipus_Incidència": tipusIncidencia,
        "Equips_i_o_Serveis_Afectats": equipsAfectats,
        "Proposta_Solucio": propostaSolucio,
        "Nivell_Urgència": nivelUrgencia,
        "Valida": valid  # Indica si la incidencia es válida o no
    }
    incidencias.append(incidencia)
    contadorTotal += 1

    contadorTotal += 1

#Calcula los porcentajes
if contadorTotal > 0:
    porcentageBuenas = (contadorBuenas / contadorTotal) * 100
    porcentageMalas = (contadorMalas / contadorTotal) * 100

    #Muestra los resultados
    print('\033[1;3;4;35m'f"\nTotal de incidencias procesadas:\033[0;35m {contadorTotal}")
    print('\033[1;3;4;32m'f"Porcentage de incidencias validas:\033[0;32m {porcentageBuenas:.2f}%")
    print('\033[1;3;4;31m'f"Porcentages de incidencias invalidas:\033[0;31m {porcentageMalas:.2f}%")
else:
    print("No se han procesado incidencias")

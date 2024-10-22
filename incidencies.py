import xml.etree.ElementTree as ET #ElementTree es una biblioteca en Python que permet analitzar i crear dades XML
from datetime import datetime

archivoXML = ET.parse("incidenciasOK.xml") #Per analitzar el arxiu XML
raiz = archivoXML.getroot() #Per obtenir el node arrel

contador = 0

for row in raiz.findall('row'): #Busca tots el elements que coincideixin amb row amb el findall
    marcaTemps = row.find('Marca_de_temps').text #Fa una busqueda de la etiqueta que hem posat i despres
    adreça = row.find('Adreça_electrònica').text
    informacio = row.find('Informació_relativa_sobre_la_protecció_de_dades_en_compliment_del_Reglament_General_de_Protecció_de_Dades__Reglament_UE_2016_679_del_Parlament_Europeu_i_del_Consell__de_27_d_abril_de_2016_').text
    nomCognom = row.find('NOM_i_COGNOMS').text
    dataIncidencia = row.find('DATA_DE_LA_INCIDÈNCIA').text
    tipusIncidencia = row.find('TIPUS_INCIDÈNCIA').text
    equipsAfectats = row.find('EQUIPS_i_o_SERVEIS_AFECTATS').text
    propostaSolucio = row.find('DESCRIPCIÓ____PROPOSTA_DE_SOLUCIÓ').text
    nivelUrgencia = row.find('NIVELL_URGÈNCIA_DE_SOLUCIÓ').text

    print(f'Marca_de_Temps: {marcaTemps}, '
          f'Adreça_electrònica: {adreça}, '
          f'Informació_relativa_sobre_la_protecció_de_dades_en_compliment_del_Reglament_General_de_Protecció_de_Dades__Reglament_UE_2016_679_del_Parlament_Europeu_i_del_Consell__de_27_d_abril_de_2016_: {informacio},'
          f'NOM_i_COGNOMS: {nomCognom}, '
          f'DATA_DE_LA_INCIDÈNCIA: {dataIncidencia}, '
          f'TIPUS_INCIDÈNCIA: {tipusIncidencia}, '
          f'EQUIPS_i_o_SERVEIS_AFECTATS: {equipsAfectats},'
          f'DESCRIPCIÓ____PROPOSTA_DE_SOLUCIÓ: {propostaSolucio},'
          f'NIVELL_URGÈNCIA_DE_SOLUCIÓ: {nivelUrgencia}')

    contador += 1
print('\033[1;3;4;35m'f'Hay {contador} incidencias')

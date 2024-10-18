import xml.etree.ElementTree as ET

archivoXML = ET.parse("incidenciasOK.xml")
raiz = archivo_XML.getroot()

for row in raiz.findall('row'):
    marcaTemps = row.find('Marca_de_temps').text
    adreça = row.find('Adreça_electrònica').text
    informacio = row.find('Informació_relativa_sobre_la_protecció_de_dades_en_compliment_del_Reglament_General_de_Protecció_de_Dades__Reglament_UE_2016_679_del_Parlament_Europeu_i_del_Consell__de_27_d_abril_de_2016_')
    nomCognom = row.find('NOM_i_COGNOMS')
    dataIncidencia = row.find('DATA_DE_LA_INCIDÈNCIA')
    tipusIncidencia = row.find('TIPUS_INCIDÈNCIA')
    equipsAfectats = row.find('EQUIPS_i_o_SERVEIS_AFECTATS')
    propostaSolucio = row.find('DESCRIPCIÓ____PROPOSTA_DE_SOLUCIÓ')
    nivelUrgencia = row.find('NIVELL_URGÈNCIA_DE_SOLUCIÓ')

    print(f'Marca_de_Temps: {marcaTemps}, '
          f'Adreça_electrònica: {adreça}, '
          f'Informació_relativa_sobre_la_protecció_de_dades_en_compliment_del_Reglament_General_de_Protecció_de_Dades__Reglament_UE_2016_679_del_Parlament_Europeu_i_del_Consell__de_27_d_abril_de_2016_: {informacio},'
          f'NOM_i_COGNOMS: {nomCognom}, '
          f'DATA_DE_LA_INCIDÈNCIA: {dataIncidencia}, '
          f'TIPUS_INCIDÈNCIA: {tipusIncidencia}, '
          f'EQUIPS_i_o_SERVEIS_AFECTATS: {equipsAfectats},'
          f'DESCRIPCIÓ____PROPOSTA_DE_SOLUCIÓ: {propostaSolucio},'
          f'NIVELL_URGÈNCIA_DE_SOLUCIÓ: {nivelUrgencia}')


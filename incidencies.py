import xml.etree.ElementTree as ET

archivo_XML = "Incidencies.xml"

arbol = ET.parse(archivo_XML)
print(arbol)
root_node = arbol.getroot()

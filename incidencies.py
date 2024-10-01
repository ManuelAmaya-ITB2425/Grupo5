import xml.etree.ElementTree as ET
tree = ET.parse('Incidencies')
root = tree.getroot()

root.tag

root.attrib

for child in root:
    print(child.tag, child.attrib)
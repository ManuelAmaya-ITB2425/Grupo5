import pandas as pd

import re

# Cargar el archivo CSV
csv_file = '/home/manuel.amaya.7e6/Baixades/incidencies.csv'  # Asegúrate de que este archivo exista
df = pd.read_csv(csv_file)

df.columns = df.columns.str.replace(' ', '_')

df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('\n', '')

df.columns = [re.sub(r'\W+', '_', col) for col in df.columns]

# Convertir a XML
xml_file = '../incidenciasOK.xml'  # Nombre del archivo XML de salida
df.to_xml(xml_file, index=False)

print(f'Archivo convertido a XML y guardado como: {xml_file}')

# Rodrigo creador

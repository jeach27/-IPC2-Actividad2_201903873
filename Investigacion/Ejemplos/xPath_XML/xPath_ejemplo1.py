import xml.etree.cElementTree as ET
tree = ET.parse('prueba.xml')
root = tree.getroot()

for estudiante in root.findall('staff'):
    name = estudiante.get('nickname')
    credit = estudiante.get('credits')
    print(name, credit)


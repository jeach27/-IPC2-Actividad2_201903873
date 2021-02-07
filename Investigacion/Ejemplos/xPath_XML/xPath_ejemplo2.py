import xml.etree.cElementTree as ET
tree = ET.parse('prueba.xml')
root = tree.getroot()

for estudiante in root.findall('staff'):
    name = estudiante.find('nickname')
    credit = estudiante.find('credits')
    print(name, credit)

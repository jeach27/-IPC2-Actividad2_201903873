from xml.dom import minidom

doc = minidom.parse("prueba.xml")

def getNodeText(node):

    nodelist = node.childNodes
    result = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            result.append(node.data)
    return ''.join(result)

name = doc.getElementsByTagName("name")[0]

print("Node Value : %s \n" % getNodeText(name))


staffs = doc.getElementsByTagName("staff")
for staff in staffs:
    sid = staff.getAttribute("id")
    nickname = staff.getElementsByTagName("nickname")[1]
    credit = staff.getElementsByTagName("credits")[0]
    print("carné:%s, nombre:%s, creditos:%s" %
    (sid, getNodeText(nickname), getNodeText(credit)))
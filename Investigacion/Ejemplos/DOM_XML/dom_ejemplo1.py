
from xml.dom import minidom

doc = minidom.parse("prueba.xml")

name = doc.getElementsByTagName("name")[0]
print(name.firstChild.data)

staffs = doc.getElementsByTagName("staff")
for staff in staffs:
        sid = staff.getAttribute("id")
        nickname = staff.getElementsByTagName("nickname")[0]
        credit = staff.getElementsByTagName("credits")[0]
        print("carné:%s, nombre:%s, creditos:%s" %
              (sid, nickname.firstChild.data, credit.firstChild.data))




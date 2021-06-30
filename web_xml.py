import xml.etree.ElementTree as ET
# データを作成
root = ET.Element('root')
tree = ET.ElementTree(element=root)

employee = ET.SubElement(root, 'employee')
# データの中身、1つ目（id:111、Mike）を作成
employ = ET.SubElement(employee, 'employ')
employ_id = ET.SubElement(employ, 'id')
employ_id.text = '111'
employ_id = ET.SubElement(employ, 'name')
employ_id.text = 'Mike'
# データの中身、2つ目（id:222、Nancy）を作成
employ = ET.SubElement(employee, 'employ')
employ_id = ET.SubElement(employ, 'id')
employ_id.text = '222'
employ_id = ET.SubElement(employ, 'name')
employ_id.text = 'Nancy'

tree.write('test.xml', encoding='utf-8', xml_declaration=True)

# データを読み出す
tree = ET.ElementTree(file='test.xml')
root = tree.getroot()

# 階層別にforでループをかける
for employee in root:
    for employ in employee:
        for person in employ:
            print(person.tag, person.text)

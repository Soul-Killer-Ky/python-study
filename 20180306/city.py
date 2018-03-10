import xml.dom.minidom as md
import xlrd

def get_xls(file):
    workbook = xlrd.open_workbook(file)
    sheet = workbook.sheet_by_index(0)
    content = {}
    for i in range(0, sheet.nrows):
        content[i+1] = sheet.row_values(i)[1:]
    return content

def write_to_xml(xls):
    xmlfile = md.Document()

    root = xmlfile.createElement('root')
    cities = xmlfile.createElement('cities')

    xmlfile.appendChild(root)
    root.appendChild(cities)

    comment = xmlfile.createComment('''
    城市信息
    ''')


    cities.appendChild(comment)

    first = xmlfile.createTextNode('{')
    cities.appendChild(first)

    for i, v in xls.items():
        xmlcontent = xmlfile.createTextNode("\t" + str(i) + ' : ' + str(v))
        cities.appendChild(xmlcontent)

    end = xmlfile.createTextNode('}')
    cities.appendChild(end)

    with open('./city.xml', 'wb') as f:
        f.write(xmlfile.toprettyxml(encoding='UTF-8'))

if __name__ == '__main__':
    write_to_xml(get_xls('./city.xls'))


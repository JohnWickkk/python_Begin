import xml.etree.ElementTree as ET

def xml_to_table(xml_data):
    root = ET.fromstring(xml_data)
    table = []
    headers = ['partner_status', 'npg_status', 'first_mile', 'last_mile']

    for item in root.findall('item'):
        row = []
        for header in headers:
            row.append(item.find(header).text)
        table.append(row)

    return table
import xml.etree.ElementTree as etree


tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

with open('result.txt', 'w', encoding='utf-8') as f:
    for source in root.iter('source'):
            f.write(source.text)
            f.write('\n')

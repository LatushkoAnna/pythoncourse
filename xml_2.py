import xml.etree.ElementTree as etree


tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

with open('result_1.txt', 'w', encoding='utf-8') as f:
    for tokens in root.iter('tokens'):
        for token in tokens.findall('token'):
            gs = []
            for g in token.iter('g'):
                gs.append(g.attrib['v'])
            if 'NOUN' in gs and 'plur' in gs:
                f.write(token.attrib['text'])
                f.write('\n')

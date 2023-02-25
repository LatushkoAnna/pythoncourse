import xml.etree.ElementTree as etree


tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

conj = 0
verb = 0
for token in root.iter('token'):
    if token.attrib['text'] == 'может':
        for g in token.iter('g'):
            if g.attrib['v'] == 'CONJ':
                conj += 1
            elif g.attrib['v'] == 'VERB':
                verb += 1
print(conj, verb)

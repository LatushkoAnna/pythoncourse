import xml.etree.ElementTree as etree


class Corpus:

    def __init__(self):
        self._sentences = []

    def load(self, path_to_corpus):
        tree = etree.parse(path_to_corpus)
        root = tree.getroot()
        for sent in root.iter('sentence'):
            sentence_string = sent.find('source').text
            sentence_words = []
            for token in sent.find('tokens'):
                wordform_string = token.get('text')
                grammems = []
                for g in token.iter('g'):
                    grammems.append(g.attrib['v'])
                word = Wordform(wordform_string, grammems)
                sentence_words.append(word)
            sentence = Sentence(sentence_string, sentence_words)
            self._sentences.append(sentence)

    def get_sentence(self, num):
        return self._sentences[num]


class Sentence:
    def __init__(self, string, wordforms):
        self._sentence = string
        self._wordforms = wordforms

    def get_word(self, num):
        return self._wordforms[num]


class Wordform:

    def __init__(self, string, grammems):
        self._wordform = string
        self._grammems = grammems

    def get_grammem(self, num):
        return self._grammems[num]


corpus = Corpus()
corpus.load('annot.opcorpora.no_ambig.xml')

print(corpus.get_sentence(-1).get_word(-1).get_grammem(-1))

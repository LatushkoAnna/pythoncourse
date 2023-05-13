import xml.etree.ElementTree as etree
import unittest


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

tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()
test_corpus = []
for sent in root.iter('sentence'):
    sentence_string = sent.find('source').text
    sentence_words = []
    for token in sent.find('tokens'):
        wordform_string = token.get('text')
        grammems = []
        for g in token.iter('g'):
            grammems.append(g.attrib['v'])
        test_word = {'text': wordform_string, 'grammems': grammems}
        sentence_words.append(test_word)
    test_sentence = {'text': sentence_string, 'words': sentence_words}
    test_corpus.append(test_sentence)


class CorpusTest(unittest.TestCase):

    def setUp(self):
        self.corpus = test_corpus

    def test_corpus(self):
        c_1 = len(self.corpus)
        c_2 = len(corpus._sentences)
        self.assertEqual(c_1, c_2)

    def test_sentences(self):
        for i in range(len(self.corpus)):
            with self.subTest(i=i):
                s_1 = self.corpus[i]['text']
                s_2 = corpus.get_sentence(i)._sentence
                self.assertEqual(s_1, s_2)

    def test_words(self):
        for i in range(len(self.corpus)):
            for j in range(len(self.corpus[i]['words'])):
                with self.subTest(i=i, j=j):
                    w_1 = self.corpus[i]['words'][j]['text']
                    w_2 = corpus.get_sentence(i).get_word(j)._wordform
                    self.assertEqual(w_1, w_2)

    def test_grammems(self):
        for i in range(len(self.corpus)):
            for j in range(len(self.corpus[i]['words'])):
                for k in range(len(self.corpus[i]['words'][j]['grammems'])):
                    with self.subTest(i=i, j=j, k=k):
                        g_1 = self.corpus[i]['words'][j]['grammems'][k]
                        g_2 = corpus.get_sentence(i).get_word(j).get_grammem(k)
                        self.assertEqual(g_1, g_2)

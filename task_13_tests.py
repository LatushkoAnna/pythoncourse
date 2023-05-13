import xml.etree.ElementTree as etree
import unittest


class CorpusTest(unittest.TestCase):

    def setUp(self):
        self.corpus = Corpus()
        self.corpus.load('annot.opcorpora.no_ambig.xml')

        tree = etree.parse('annot.opcorpora.no_ambig.xml')
        root = tree.getroot()
        self.test_corpus = []
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
            self.test_corpus.append(test_sentence)

    def test_corpus(self):
        c_1 = len(self.test_corpus)
        c_2 = len(self.corpus.get_sent_list())
        self.assertEqual(c_1, c_2)

    def test_sentences(self):
        for i in range(len(self.test_corpus)):
            with self.subTest(i=i):
                s_1 = self.test_corpus[i]['text']
                s_2 = self.corpus.get_sentence(i).get_sent_text()
                self.assertEqual(s_1, s_2)

    def test_words(self):
        for i in range(len(self.test_corpus)):
            for j in range(len(self.test_corpus[i]['words'])):
                with self.subTest(i=i, j=j):
                    w_1 = self.test_corpus[i]['words'][j]['text']
                    w_2 = self.corpus.get_sentence(i).get_word(j).get_wordform()
                    self.assertEqual(w_1, w_2)

    def test_grammems(self):
        for i in range(len(self.test_corpus)):
            for j in range(len(self.test_corpus[i]['words'])):
                for k in range(len(self.test_corpus[i]['words'][j]['grammems'])):
                    with self.subTest(i=i, j=j, k=k):
                        g_1 = self.test_corpus[i]['words'][j]['grammems'][k]
                        g_2 = self.corpus.get_sentence(i).get_word(j).get_grammem(k)
                        self.assertEqual(g_1, g_2)

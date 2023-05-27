import json
import unittest
from collections import Counter

import pymorphy2

from task_14 import TFIDF


class TFIDFTest(unittest.TestCase):

    def setUp(self):
        self.object = TFIDF(['text_1.txt', 'text_2.txt', 'text_3.txt'])
        self.tfidfs = self.object.count_tfidf('user_text.txt')
        self.zeroed_tfidfs = self.object.count_tfidf('text_with_all_new_words.txt')

        morph = pymorphy2.MorphAnalyzer()
        with open('user_text.txt', 'r', encoding='utf-8') as f:
            text = f.read()
        for sym in '.,:;«»“”!?—"_()<>\n':
            text = text.replace(sym, '')
        temp = text.lower().split()
        words = [morph.parse(word)[0].normal_form for word in temp]
        self.words_count = Counter(words)

        with open('idfs.json', 'r', encoding='utf-8') as f:
            self.idfs = json.load(f)

    def test_len_texts(self):
        self.assertEqual(len(self.words_count), len(self.tfidfs))

    def test_idfs_not_in_file(self):
        for word_tfidf_pair in self.zeroed_tfidfs:
            with self.subTest(word_tfidf_pair=word_tfidf_pair):
                self.assertFalse(word_tfidf_pair[-1])

    def test_loading_idfs(self):
        for word in self.idfs:
            with self.subTest(word=word):
                self.assertEqual(self.idfs[word], self.object.get_idfs()[word])

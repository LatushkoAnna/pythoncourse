import json
import math
import os
from collections import Counter

import pymorphy2


class TFIDF:

    def __init__(self, paths: list):
        self._texts = []
        self._idfs = {}
        for path_to_file in paths:
            self._add_text(path_to_file)
        if os.path.exists('idfs.json'):
            with open('idfs.json', 'r', encoding='utf-8') as f:
                self._idfs = json.load(f)
        else:
            for text in self.get_texts():
                self._count_idfs(text)

    def get_texts(self):
        return self._texts

    def get_idfs(self):
        return self._idfs

    def _add_text(self, path_to_file):
        words_count = Counter(self._preprocess(path_to_file))
        self._texts.append(words_count)

    def _preprocess(self, path_to_file):
        morph = pymorphy2.MorphAnalyzer()
        with open(path_to_file, 'r', encoding='UTF-8') as f:
            text = f.read()
        for sym in '.,:;«»“”!?—"_()<>\n':
            text = text.replace(sym, '')
        temp = text.lower().split()
        words = [morph.parse(word)[0].normal_form for word in temp]
        return words

    def _count_idfs(self, text):
        for word in text:
            d = len(self._texts)
            di = 0
            for text in self._texts:
                if word in text:
                    di += 1
            self._idfs[word] = math.log(abs(d) / abs(di))
        with open('idfs.json', 'w', encoding='utf-8') as f:
            json.dump(self.get_idfs(), f, ensure_ascii=False, indent=4)

    def count_tfidf(self, path_to_file):
        words = self._preprocess(path_to_file)
        words_count = Counter(words)
        tfidfs = []
        text_len = len(words)
        for word in words:
            tf = words_count[word] / text_len
            idf = self._idfs.get(word, 0)
            tfidf = tf * idf
            tfidfs.append((word, tfidf))
        return tfidfs

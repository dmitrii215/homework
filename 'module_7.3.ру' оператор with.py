'''задача: найдет всё'''
class WordsFinder:
    def __init__(self, *file_name):
        self.file_names = [*file_name]
        self.file_name = file_name

    def get_all_words(self):
        all_words = {}
        words = []
        simbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as open_:
                for line in open_:
                    line = line.lower()
                    for p in simbols:
                        if p in line:
                            line = line.replace(p, ' ')
                    split_line = line.split(sep=' ')
                    words.append(split_line)
        sorted_words = [x for y in words for x in y]
        all_words[self.file_name] = sorted_words
        return all_words

    def find(self, word):
        dict_ = {}
        for name, words in self.get_all_words().items():
            for w in words:
                if word.lower() in w:
                    index = words.index(w)
                    dict_[self.file_name] = index + 1
                    break
        return dict_

    def count(self, word):
        dict_ = {}
        count = 0
        for name, words in self.get_all_words().items():
            for w in words:
                if word.lower() in w:
                    count += 1
        dict_[self.file_name] = count
        return dict_

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего








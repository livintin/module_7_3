class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)
        self.punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    for i in self.punctuation:
                        line = line.replace(i, ' ')
                    words.extend(line.split())
                    all_words[file_name] = words
        return all_words

    def find(self, word):
        first_words = {}
        word = word.lower()
        for key, value in self.get_all_words().items():
            if word in value:
                first_words[key] = value.index(word) + 1
        return first_words

    def count(self, word):
        count_words = {}
        word_count = []
        word = word.lower()
        for key, value in self.get_all_words().items():
            word_count.extend(value)
            count_words[key] = word_count.count(word)
        return count_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

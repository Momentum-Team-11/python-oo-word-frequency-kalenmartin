import string
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_contents(self):
        with open(self.filename) as file:
            text_string = file.read()

        return text_string


class WordList:
    def __init__(self, text_string):
        self.list = []
        self.text = text_string
        self.longest_word_length = 0

    def extract_words(self):
        self.list = self.text.lower().strip().split()
        transformed_words = []
        for word in self.list:
            if word not in STOP_WORDS:
                transformed_words.append(word.strip(string.punctuation))
        self.list = transformed_words

    def set_longest_word_length(self, word):
        if len(word) > self.longest_word_length:
            self.longest_word_length = len(word)

    def get_freqs(self):
        word_count = {}
        for word in self.list:
            self.set_longest_word_length(word)
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1

        return word_count


class FreqPrinter:
    def __init__(self, freqs, longest_word_length):
        self.freqs = freqs
        self.left_margin = longest_word_length + 1

    def use_count_as_key(self, items):
        return items[1]

    def print_freqs(self):
        working_words = sorted(self.freqs.items(), key=lambda seq: seq[1], reverse = True)
        for words, count in working_words:
            print(f"{words:>20} | {(count)} {(count * '*'):<20}")



if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
            description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list = WordList(reader.read_contents())
        word_list.extract_words()
        word_list.get_freqs()
        printer = FreqPrinter(word_list.get_freqs(), word_list.longest_word_length)
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
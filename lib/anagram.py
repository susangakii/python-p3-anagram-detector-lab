# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        matches = []
        sorted_original = sorted(self.word.lower())

        for w in word_list:
            if sorted(w.lower()) == sorted_original:
                matches.append(w)

        return matches

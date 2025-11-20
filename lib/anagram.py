class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, word_list):
        matches = []
        for candidate in word_list:
            candidate_lower = candidate.lower()
            if sorted(candidate_lower) == self.sorted_word and candidate_lower != self.word:
                matches.append(candidate)
        return matches

import unittest

from challenges import words_samesum_noletters, find_unique_char_words, find_unique_char_words_by_sum, get_word_list


class LettersumTests(unittest.TestCase):
    def setUp(self) -> None:
        self.word_sets_188 = set()
        self.word_sets_188.add(frozenset({'cytotoxicity', 'unreservedness'}))
        self.word_sets_194 = [
            {'photomicrographic', 'defenselessnesses'},
            {'defenselessnesses', 'microphotographic'}
        ]
        self.word_sets = list(self.word_sets_188) + self.word_sets_194

        with open("words_188.txt") as f:
            self.word_list_188 = f.read().splitlines()
        with open("words_194.txt") as f:
            self.word_list_194 = f.read().splitlines()        

    def test_find_unique_char_words(self):
        print("Testing just the word_lists")
        self.assertEqual(find_unique_char_words(self.word_list_188), self.word_sets_188)
        test_sets = find_unique_char_words(self.word_list_194)
        for word_set in self.word_sets_194:
            self.assertIn(word_set, test_sets)

    def test_get_word_list(self):
        print("Testing the word lists from the dictionary")
        self.assertEqual(set(get_word_list(188)), set(self.word_list_188))
        self.assertEqual(set(get_word_list(194)), set(self.word_list_194))

    def test_188(self):
        print("Testing find_unique_char_words for 188")
        self.assertEqual(find_unique_char_words_by_sum(188), self.word_sets_188)

    def test_194(self):
        print("Testing find_unique_char_words for 194")
        test_sets = find_unique_char_words_by_sum(194)
        for word_set in self.word_sets_194:
            self.assertIn(word_set, test_sets)

    def test_words_samesum_noletters(self):
        lettersum = 188
        # word_sets = [
        #     {'cytotoxicity', 'unreservedness'},
        #     {'photomicrographic', 'defenselessnesses'},
        #     {'defenselessnesses', 'microphotographic'}
        # ]
        test_sets = words_samesum_noletters(lettersum)
        print("Printing test_sets")
        print(test_sets)

        for word_set in self.word_sets:
            print(f'testing {word_set}')
            self.assertIn(word_set, test_sets)
        # self.assertTrue(all(item in test_sets for item in word_sets) )

    def test_reliability(self):
        self.test_words_samesum_noletters()
        for _ in range(100):
            self.test_words_samesum_noletters()


if __name__ == "__main__":
    unittest.main()

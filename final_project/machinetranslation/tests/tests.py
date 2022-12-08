import unittest

from translator import french_to_english, english_to_french

class Testfrench_toenglish(unittest.TestCase):
            def test1(self):
                self.assertEqual(french_to_english("Bonjour"), "Hello")
                self.assertEqual(french_to_english(""), "none")

class Testenglishtofrenh(unittest.TestCase):
            def test(self):
                self.assertEqual(english_to_french("Hello"), "Bonjour")
                self.assertEqual(english_to_french(""), "none")




if __name__ == '__main__':
    unittest.main()
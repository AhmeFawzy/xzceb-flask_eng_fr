import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertEqual(englishToFrench('How are you'), 'comment allez-vous')
        self.assertEqual(englishToFrench('Goodbye'), 'Au revoir')

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(frenchToEnglish('comment allez-vous'), 'How are you')
        self.assertEqual(frenchToEnglish('Au revoir'), 'Goodbye')

unittest.main()

import unittest
import number_to_words as n

class FuncTest(unittest.TestCase):
    def test_get_higher(self):
        tests = [
            [[1, 1], " tisíc"],
            [[2, 1], " milion"],
            [[3, 1], " miliarda"],
            [[1, 2], " tisíce"],
            [[2, 2], " miliony"],
            [[3, 2], " miliardy"],
            [[1, 5], " tisíc"],
            [[2, 5], " milionů"],
            [[3, 5], " miliard"],
        ]
        for i in tests:
            self.assertEqual(n.get_higher(*i[0]), i[1])
            
    def test_get_for_am(self):
        tests = [
            [[1, 100], "sto"],
            [[2, 100], "stě"],
            [[3, 100], "sta"],
            [[8, 100], "set"],
            [[1, 1000], "tisíc"],
            [[2, 1000], "tisíce"],
            [[4, 1000], "tisíce"],
            [[5, 1000], "tisíc"],
        ]
        for i in tests:
            self.assertEqual(n.get_for_am(*i[0]), i[1])
            
    def test_get_ones(self):
        tests = [
            [[0, 0, False], ""],
            [[0, 5121, True], ""],
            [[1, 0, False], "jedna"],
            [[1, 2, False], "jeden"], # jeden milion
            [[1, 3, False], "jedna"], # jedna miliarda
            [[2, 0, False], "dva"],
            [[2, 0, True], "dvě"], # dvě stě
            [[2, 2, False], "dva"], # dva miliony
            [[2, 3, False], "dvě"], # dvě miliardy
            [[14, 0, False], "čtrnáct"],
            [[14, 415, False], "čtrnáct"],
        ]
        for i in tests:
            self.assertEqual(n.get_ones(i[0][0], ind=i[0][1], hun=i[0][2]), i[1])
            
    def test_get_tens(self):
        tests = [
            [[10], "deset"],
            [[45], "čtyřicet pět"],
            [[17], "sedmnáct"],
            [[99], "devadesát devět"],
            [[50], "padesát"],
        ]
        for i in tests:
            self.assertEqual(n.get_tens(*i[0]), i[1])
            
    def test_get_hundereds(self):
        tests = [
            [[1], "sto"],
            [[2], "dvě stě"],
            [[3], "tři sta"],
            [[4], "čtyři sta"],
            [[5], "pět set"],
            [[17], "sedmnáct set"],
        ]
        for i in tests:
            self.assertEqual(n.get_hundereds(*i[0]), i[1])

    def test_from_0_to_999(self):
        tests = [
            [[1, 0], "jedna"],
            [[1, 1], "jeden"], # jeden tisíc
            [[2, 1], "dva"], # dva tisíce
            [[1, 2], "jeden"], # jeden milion
            [[1, 3], "jedna"], # jedna miliarda
            [[2, 3], "dvě"], # dvě miliardy
            [[11, 0], "jedenáct"],
            [[24, 0], "dvacet čtyři"],
            [[111, 0], "sto jedenáct"],
            [[958, 0], "devět set padesát osm"],
        ]
        for i in tests:
            self.assertEqual(n.from_0_to_999(*i[0]), i[1])
            
    def test_cislo_na_text(self):
        tests = [
            [0, "nula"],
            [1, "jedna"],
            [1_000_000, "milion"],
            [1_000_001, "milion jedna"],
            [1_001_001, "milion jeden tisíc jedna"],
            [99_854_012, "devadesát devět milionů osm set padesát čtyři tisíc dvanáct"],
            [1234, "tisíc dvě stě třicet čtyři"],
            [9*10**65, "devět set deciliard"],
            [-0, "nula"],
            [-1, "mínus jedna"],
            [-99_854_012, "mínus devadesát devět milionů osm set padesát čtyři tisíc dvanáct"],
        ]
        for i in tests:
            self.assertEqual(n.cislo_na_text(i[0]), i[1])
            
if __name__ == "__main__":
    unittest.main()

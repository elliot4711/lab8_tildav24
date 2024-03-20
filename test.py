
"""
from linkedQfile import LinkedQ

que = LinkedQ()

que.enqueue("a")
que.enqueue("b")

print(que.peek())
print(que.dequeue())
print(que.dequeue())
"""


import unittest

from main import *

class SyntaxTest(unittest.TestCase):

    def test1(self):
        """ Testar Subj och Pred """
        self.assertEqual(ismolecule("H2"), "Formeln är syntaktiskt korrekt")

    def test2(self):
        """ Testar Subj och Pred """
        self.assertEqual(ismolecule("P21"), "Formeln är syntaktiskt korrekt")

    def test3(self):
        """ Testar Subj och Pred """
        self.assertEqual(ismolecule("Ag3"), "Formeln är syntaktiskt korrekt")
    
    def test4(self):
        """ Testar Subj och Pred """
        self.assertEqual(ismolecule("Fe12"), "Formeln är syntaktiskt korrekt")

    def test5(self):
        """ Testar Subj och Pred """
        self.assertEqual(ismolecule("Xx5"), "Formeln är syntaktiskt korrekt")
    
    def test6(self):
        """ Testar Subj och Pred """
        self.assertEqual(ismolecule("H10100"), "Formeln är syntaktiskt korrekt")

    def test7(self):
        """ Testar Subj och Pred """
        self.assertEqual(ismolecule("a"), "Saknad stor bokstav vid radslutet a")

    def test8(self):
        """ Testar Subj och Pred """
        self.assertEqual(ismolecule("cr12"), "Saknad stor bokstav vid radslutet cr12")

    def test9(self):
        """ Testar Subj och Pred """
        self.assertEqual(ismolecule("8"), "Saknad stor bokstav vid radslutet 8")

    def test10(self):
        """ Testar Subj och Pred """
        self.assertEqual(ismolecule("Cr0"), "För litet tal vid radslutet")

    def test11(self):
        """ Testar Subj och Pred """
        self.assertEqual(ismolecule("Pb1"), "För litet tal vid radslutet")

    def test12(self):
        """ Testar Subj och Pred """
        self.assertEqual(ismolecule("H01011"), "För litet tal vid radslutet 1011")

if __name__ == '__main__':
    unittest.main()



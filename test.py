
"""
from linkedQfile import LinkedQ

que = LinkedQ()

que.enqueue("a")
que.enqueue("b")

print(que.peek())
print(que.dequeue())
print(que.dequeue())
"""
'''
import unittest

from main import *

class SyntaxTest(unittest.TestCase):

    def testSubjPred(self):
        """ Testar Subj och Pred """
        self.assertEqual(ismolecule("Korrekt molekyl"), "Vår output")

    def testFelKonj(self):
        self.assertEqual(ismolecule("Felaktig molekyl"), "Vår output")

if __name__ == '__main__':
    unittest.main()

'''

import re
def has_numbers(inputString):
    return bool(re.search(r'\d', inputString))

print(has_numbers("He12"))
# True
print(has_numbers("He"))
# False


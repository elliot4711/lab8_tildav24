
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

from linkedQfile import LinkedQ
import re

def ismolecule(molecule):
    x = re.search(r'\d', molecule)
    que = LinkedQ()
    for letter in molecule:
        que.enqueue(letter)

    if x:
        que2 = isatom(que)
        isnum(que2)
        return("Formeln är syntaktiskt korrekt")
    
    else:
        isatom(que)
        return("Formeln är syntaktiskt korrekt")
    

def isatom(que):
    y = que.peek()
    x = que.dequeue()
    if isbigletter(x):
        if y == None:
            return que
        else: 
            z = re.search(r'\d', y)
            if z:
                return que
            
            else:
                y = que.dequeue()
                if issmallletter(y):
                    return que
                else:
                    raise Syntaxfel("Något är fel")
            
    else:
        word = x
        while not que.isEmpty():
            l = que.dequeue()
            word += l
        raise Syntaxfel(f"Saknad stor bokstav vid radslutet {word}")


def isbigletter(value):
    x = re.search("[A-Z]", value)
    if x:
        return True
    else:
        return False 

def issmallletter(value):
    x = re.search("[a-z]", value)
    if x:
        return True
    else:
        return False      

def isnum(que):
    z = que.peek()
    y = que.dequeue()
    x = re.search("[2-9]", y)
    if x:
        return True
    elif y == "0":
        word = ""
        if not que.isEmpty():
            while not que.isEmpty():
                l = que.dequeue()
                word += l
            raise Syntaxfel(f"För litet tal vid radslutet {word}")
        else:
            raise Syntaxfel("För litet tal vid radslutet")
    elif y == "1":
        if z == None:
            raise Syntaxfel("För litet tal vid radslutet")
        else:
            number = re.search(r'\d', z) #Skapar problem
            if number:
                pass
            else:
                raise Syntaxfel("För litet tal vid radslutet")
    else:
        print("fel")

class Syntaxfel(Exception):
    """
    Exception for when syntax is wrong, inherits from Exception
    """

    pass


def testfunc(molecule):
    try:
        value = ismolecule(molecule)
        return value
    except Syntaxfel as err:
        returnvalue = str(err.args[0])
        return returnvalue


class SyntaxTest(unittest.TestCase):

    def test1(self):
        
        self.assertEqual(testfunc("H2"), "Formeln är syntaktiskt korrekt")

    def test2(self):
        
        self.assertEqual(testfunc("P21"), "Formeln är syntaktiskt korrekt")

    def test3(self):
        
        self.assertEqual(testfunc("Ag3"), "Formeln är syntaktiskt korrekt")
    
    def test4(self):
        
        self.assertEqual(testfunc("Fe12"), "Formeln är syntaktiskt korrekt")

    def test5(self):
        
        self.assertEqual(testfunc("Xx5"), "Formeln är syntaktiskt korrekt")
    
    def test6(self):
        
        self.assertEqual(testfunc("H10100"), "Formeln är syntaktiskt korrekt")

    def test7(self):
        
        self.assertEqual(testfunc("a"), "Saknad stor bokstav vid radslutet a")

    def test8(self):
        
        self.assertEqual(testfunc("cr12"), "Saknad stor bokstav vid radslutet cr12")

    def test9(self):
        
        self.assertEqual(testfunc("8"), "Saknad stor bokstav vid radslutet 8")

    def test10(self):
        
        self.assertEqual(testfunc("Cr0"), "För litet tal vid radslutet")

    def test11(self):
        
        self.assertEqual(testfunc("Pb1"), "För litet tal vid radslutet")

    def test12(self):
        
        self.assertEqual(testfunc("H01011"), "För litet tal vid radslutet 1011")

if __name__ == '__main__':
    unittest.main()



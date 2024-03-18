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
        print("Formeln är syntaktiskt korrekt")
    
    else:
        isatom(que)
        print("Formeln är syntaktiskt korrekt")
    

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
        raise Syntaxfel("Saknad stor bokstav vid radslutet")


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
        raise Syntaxfel("För litet tal vid radslutet")
    elif y == "1":
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

take_input = True
while take_input == True:
    molecule = input("")
    if molecule == ("#"):
        take_input = False
    else:
        ismolecule(molecule)


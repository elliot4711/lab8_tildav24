from linkedQfile import LinkedQ
import re

def ismolecule(molecule):
    """ 
    Function for testing if input follows syntax for a molecule
    Parameters: text that could be a molecule
    Returns: nothing
    """


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
    """ 
    Function for testing if input follows syntax for an atom
    Parameters: linkedQ object containing all letters and numbers in the atom name
    Returns: linkedQ object with only numbers remaining
    """

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
    """ 
    Function for testing if a value is a capital letter
    Parameters: value to check
    Returns: True or False
    """

    x = re.search("[A-Z]", value)
    if x:
        return True
    else:
        return False 

def issmallletter(value):
    """ 
    Function for testing if a value is a lowercase letter
    Parameters: value to check
    Returns: True or False
    """

    x = re.search("[a-z]", value)
    if x:
        return True
    else:
        return False      

def isnum(que):
    """ 
    Function for testing if input follows syntax for a number higher or equal to 2
    Parameters: linkedQ object containing all numbers in the atom name
    Returns: True if number is higher or equal to 2
    """

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
            number = re.search(r'\d', z)
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
        try:
            returnvalue = ismolecule(molecule)
        except Syntaxfel as err:
            returnvalue = str(err.args[0])
            print(returnvalue)

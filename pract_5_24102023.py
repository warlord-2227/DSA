"""
Write a class which has atleast two methods
getstring and printstring and have a test method to check class is working fine
getstring: to get string from input
printstring: print string in upper case
"""

class FirstClass():
    def __init__(self):
        self.str1 = ""
    def getstring(self,):
        print("Enter string here")
        self.str1 = input()
    def printstring(self,):
        return self.str1.upper()

def test_class():
    check = FirstClass()
    check.getstring()
    print(check.printstring())

test_class()


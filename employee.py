__author__ = 'Nickolas'
from ss import *


class Employee:
    def __init__(self,last=None, first=None, start=None, payrate=None, social=None):
        if (last is None) and (first is None) and (start is None) and (payrate is None) and (social is None):
            self.last=input("Last Name:")
            self.first=input("First Name:")
            self.start=input("Start Year:")
            self.payrate=input("Pay Rate:")
            self.social= SS()
        else:
            self.last=last.capitalize()
            self.first=first.capitalize()
            self.start=start
            self.payrate=float(payrate)
            self.social = SS(social)

    def __str__(self):
        return(self.first+" "+self.last+" "+"began working in the year "+self.start+", makes "+str(self.payrate)+" dollars an hour "+
               "and social security number is "+self.social.ss)
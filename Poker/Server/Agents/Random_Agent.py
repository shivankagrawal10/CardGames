
import math
from random import randint, random

class Agent:
    def getDecision(self):
        return randint(0,2)

    def getRaise(self,balance):
        return math.ceil(random()*balance)+1
import sys
from Agents import complexAgent

class player:
    def __init__(self,name):
        self.name = name
        self.is_agent = 0
        self.agent_type = None
        self.cards = []
        self.money = 0
        self.current_bet = 0                                   #Particular round bet ()
        self.game_bet = 0                                   #Sum of all rounds bet (1 full game of 5 cards)
        self.round_bet = 0
        '''if self.is_agent == 1:
            self.agent_type = Agents.Random_Agent()
        elif self.is_agent == 2:
            self.agent_type = Agents.complexAgent()'''
        #self.net = ntwk.Network()

    def updateAgentInfo(self,pot, hole_cards, round_bet):
        self.round_bet = round_bet
        self.agent_type.updateInfo(pot,hole_cards, self.cards, self.money, round_bet)

    def getDecision(self):
        if(self.is_agent == 0):
            inp = int(input())
            while(inp != 0 and inp != 1 and inp != 2):
                print(f"Try Again: Enter #: 0 - Fold, 1 - Call, 2 - Raise",file=sys.stderr)
                inp = int(input())
            return inp
        else:
            dec = self.agent_type.getDecision()
            if(self.money < self.round_bet):
                while(dec == 2):
                    dec = self.agent_type.getDecision()
            return dec
    
    def getRaise(self):
        if(self.is_agent == 0):
            return int(input())
        else:
            return self.agent_type.getRaise()

    def setAgent(self,agent_type):
        self.is_agent = agent_type
        if self.is_agent != 0:
            self.agent_type = complexAgent.Agent()

    def setCurrentBet(self,amount):
        diff = amount - self.current_bet
        print(f"difference {diff}")
        self.current_bet = amount
        if(diff >= 0):    
            self.game_bet += diff
            self.__adjustAccount__(diff)
            return diff
        return amount

    def getCurrentBet(self):
        return self.current_bet

    def set_money(self,money):                              #To only be accessed by game program
        self.money = money
        if self.is_agent != 0:
            self.agent_type.set_money(money)
    
    def getMoney(self):
        return self.money

    def set_cards(self,cards):
        self.cards = cards
    
    def __adjustAccount__(self,amount):           
        self.money -= amount

    def fold(self):
        temp = self.cards
        self.cards = []
        self.current_bet = 0
        return temp

    def __str__(self):
        if(self.cards):
            return f"{self.name.ljust(10)} - {self.cards[0].__str__().ljust(10)}, {self.cards[1].__str__().ljust(11)} - ${self.money}"
        else:
            return f"{self.name.ljust(10)} - No Cards - ${self.money}"


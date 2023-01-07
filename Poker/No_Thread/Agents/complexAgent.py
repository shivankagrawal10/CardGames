import numpy as np
import math
from random import randint, random
import winningHand

class Agent:
    def __init__(self, agent_type=0):
        self.__agent_type__ = agent_type
        self.pot = 0
        self.hole_cards = []                    #alternatively only consider the value of hand you may have
        self.value_of_hand = -1                 #-1 means not enough info
        self.number_players = 0
        self.qtable = np.zeros((10,3))
        self.own_cards = []
        self.money = 0
        #self.current_bet = 0                                   #Particular round bet ()
        #self.game_bet = 0                                   #Sum of all rounds bet (1 full game of 5 cards)

        self.checkerObject = winningHand
        self.action = 0

        self.alpha = 0.1
        self.gamma = 1
        self.epsilon = 0.1

    def set_money(self,money):
        self.money = money

    def updateInfo(self, pot, hole_cards, own_cards, money, round_bet):
        self.pot = pot
        self.hole_cards = hole_cards
        self.own_cards = own_cards
        money_diff = self.money - money
        self.money = money
        self.round_bet = round_bet
        self.checker = winningHand.checker(self.hole_cards+self.own_cards)
        old_state = self.value_of_hand
        old_val = self.qtable[self.value_of_hand,self.action]
        self.value_of_hand = self.checker.check()
        next_max = np.max(self.qtable[self.value_of_hand])
        new_val = (1-self.alpha) * old_val + self.alpha * (money_diff + self.gamma * next_max)
        self.qtable[old_state,self.action] = new_val

    def getDecision(self):
        if(self.__agent_type__ == 0):
            return randint(0,2)
        if(self.__agent_type__ == 1):
            state = self.value_of_hand
            if random.uniform(0,1) < self.epsilon:
                self.action = randint(0,2)
            else:
                self.action = np.argmax(self.qtable[state])
            return self.action

    def getRaise(self):
        return min(self.round_bet+10, self.money)
        #return randint(self.round_bet+1,self.round_bet+10)
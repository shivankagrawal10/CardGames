'''
Represent hand's state --> check if state is == winning hand
'''
class checker():
    def __init__(self, hand):
        self.hand_len = 7
        self.num_rep = dict()
        self.col_rep = dict()
        self.coord = []
        for i in hand:
            if(i.number+2 not in self.num_rep):
                self.num_rep[i.number+2] = 1
            else:     
                self.num_rep[i.number+2] += 1
            if(i.suite not in self.col_rep):
                self.col_rep[i.suite] = 1
            else:     
                self.col_rep[i.suite] += 1
            self.coord.append((i.number+2,i.suite))
        self.coord.sort(key=lambda x: x[0])
        self.diff = [self.coord[i+1][0]-self.coord[i][0] for i in range(7-1)]
        #for i in hand:
        #    print(i.__str__())
        #print(self.num_rep)
        #print(self.col_rep)
                
            
    def RoyalFlush(self):
        val = self.StraightFlush()
        if(val == 0):
            return 0
        
        elif(val < 9):              #tells if hand is Straight or Flush
            return val

        seq = ["10","J","Q","K","A"]
        for i in seq:               #tells if hand is Straigh Flush
            if i not in self.num_rep:
                return val

        return 10                   #tells if hand is Royal Flush

    def StraightFlush(self):
        val = 0
        flush = self.Flush()
        stra = self.Straight()
        if(flush == 0 and stra != 0):
            return stra
        elif(flush != 0 and stra == 0):
            return flush
        elif(flush == 0 and stra == 0):
            return 0
        return 9

    def FourofKind(self):
        if 4 in self.num_rep.values():
            return 8
        return 0
    
    def FullHouse(self):
        if (3 in self.num_rep.values() and 2 in self.num_rep.values()) or list(self.num_rep.values()).count(3)==2:
            return 7
        return 0
    
    def Flush(self):
        if 5 in self.col_rep.values():
            return 6
        return 0
    
    def Straight(self):
        if(self.diff[0] != 1 and self.diff[self.hand_len-2] != 1):
            return 0
        for i in range(self.hand_len-1): #len(self.diff) = self.hand_len-1
            if((i>=1 and i<=self.hand_len-3) and self.diff[i]!=1):
                return 0
        return 5
    
    def ThreeofKind(self):
        if 3 in self.num_rep.values():
            return 4
        return 0
    
    def TwoPair(self):
        if list(self.num_rep.values()).count(2)>=2:
            return 3
        return 0
    
    def OnePair(self):
        if 2 in self.num_rep.values():
            return 2
        return 0
    
    def check(self):
        wins = [self.RoyalFlush(), self.StraightFlush(),
                self.FourofKind(), self.FullHouse(),
                self.Flush(), self.Straight(), self.ThreeofKind(),
                self.TwoPair(), self.OnePair()]
        hand_names = ["RoyalFlush", "StraightFlush",
                "FourofKind", "FullHouse",
                "Flush", "Straight", "ThreeofKind",
                "TwoPair", "OnePair", "None"]
        hand_names.reverse()
        val = 0
        for i in wins:
            val = i
            if(val != 0):
                #print(hand_names[val-1])
                return val
        #print(hand_names[val])
        return val
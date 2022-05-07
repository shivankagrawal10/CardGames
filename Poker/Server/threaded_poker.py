import sys
import deck
import winningHand
import player as pl

gthread_dict = dict()
class poker:
    def __init__(self, big_blind, buy_in):
        self.pot = 0
        self.num_players = 0
        self.players = []
        self.player_name = dict()                           #count of players with same name
        self.player_address = dict()
        self.deck = deck.deck()
        self.big_blind = big_blind
        self.buy_in_amt = buy_in
        self.sb = 0
        self.bb = 1                                         #big blind position
        self.discard_pile = []
        self.hole_cards = []
        self.round_bet = 0

    def add_player (self,name,addr):
        global gthread_dict
        if name in self.player_name:
            p(f"{name} already exists, please enter another name", file =sys.stderr)
            return -1
        else:
            #print(f"reached",file=sys.stderr)
            self.players.append(pl.player(name))
            self.player_name[name] = self.num_players
            
            self.player_address[name] = addr
            
            self.num_players += 1
            p(f"{name} address is {self.player_address[name]}", file =sys.stderr)
            self.buy_in(self.players[self.num_players-1])
            p(f"{name} Buying in at ${self.buy_in_amt}", file =sys.stderr)
            gthread_dict = self.player_address
            return 0

    def buy_in(self,player:pl.player):
        player.set_money(self.buy_in_amt)

    def start_game(self):
        if(self.num_players < 2):
            p("Not enough players", file=sys.stderr)
        
        while(self.num_players > 1):

            p(f"Starting new round of poker\n", file=sys.stderr)
            self.show_players()

            self.players[self.sb].curr_bet += self.big_blind//2
            self.pot += self.players[self.sb].bet(self.big_blind//2)
            p(f"{self.players[self.sb].name} paid ${self.big_blind//2} small blind", file=sys.stderr)
            self.players[self.bb].curr_bet += self.big_blind
            self.pot += self.players[self.bb].bet(self.big_blind)
            p(f"{self.players[self.bb].name} paid ${self.big_blind} big blind\n", file=sys.stderr)

            self.deck.riffleshuffle(8)
            self.distribute_cards()

            for i in range(3):
                self.hole_cards.append(self.deck.pile.pop())

            self.discard_pile.append(self.deck.pile.pop())      #Burn Pre Turn
            self.hole_cards.append(self.deck.pile.pop())        #Add Turn Card
            self.discard_pile.append(self.deck.pile.pop())      #Burn Pre River
            self.hole_cards.append(self.deck.pile.pop())        #Add River Card

            round_order = []
            round_ord_len = self.num_players
            round_index = self.sb
            winner = [-1]
            for i in self.players:
                round_order.append(self.players[round_index])
                round_index = (round_index+1) % self.num_players
            
            for i in range(4):
                if(round_ord_len == 1):
                    winner = [0]
                    break

                betting_over = 0                                #Boolean whether betting is still live
                curr_player = 0
                if(i == 0):                                     #i=0 is the pre-flop round
                    round_index = 2                             #first player is next to big blind
                    self.round_bet = self.big_blind
                else:                                           #i>0 if post flop rounds
                    round_index = 0                             #first player is small blind
                    self.round_bet = 0
                    for pl in round_order:
                        pl.curr_bet = 0

                curr_player = self.player_name[round_order[round_index].name]
                last_player = round_order[(round_index-1)%round_ord_len].name
                
                #self.show_players()
                self.show_hole_cards(i)                         #showing players which round it is
                
                while(betting_over == 0):
                    if(round_ord_len == 1):
                        winner = [0]
                        break
                    if(self.players[curr_player].name == last_player):
                        betting_over = 1
                    
                    p(f"Turn: {self.players[curr_player].name}",file=sys.stderr)
                    
                    p(self.players[curr_player].__str__())
                    thread_send(self.players[curr_player].name, "Enter #: 0 - Fold, 1 - Call, 2 - Raise")
                    inp = int(thread_receive(self.players[curr_player].name))
                    '''
                    p(f"Enter #: 0 - Fold, 1 - Call, 2 - Raise")
                    inp = int(input())
                    while(inp != 0 and inp != 1 and inp != 2):
                        p(f"Try Again: Enter #: 0 - Fold, 1 - Call, 2 - Raise",file=sys.stderr)
                        inp = int(input())
                    p("",file=sys.stderr)
                    '''
                    if(inp == 0):
                        fold = self.players[curr_player].fold()
                        while fold:
                            self.discard_pile.append(fold.pop())
                        self.players[curr_player].curr_bet = 0
                        if(self.players[curr_player].name == last_player):
                            betting_over = 1
                        round_order.pop(round_index)
                        round_ord_len -= 1
                        round_index = round_index % round_ord_len
                        
                    elif(inp == 1):
                        diff = self.round_bet - self.players[curr_player].curr_bet
                        self.players[curr_player].money -= diff
                        self.pot += diff
                        self.players[curr_player].curr_bet = self.round_bet
                        round_index = (round_index+1) % round_ord_len
                    else:
                        raise_val = int(input("Enter amount you want to raise the current round betting size: "))
                        diff = (self.round_bet + raise_val) - self.players[curr_player].curr_bet
                        self.players[curr_player].money -= diff
                        self.pot += diff
                        self.round_bet += raise_val
                        self.players[curr_player].curr_bet = self.round_bet
                        last_player = round_order[(round_index-1)%round_ord_len].name
                        round_index = (round_index+1) % round_ord_len
                        betting_over = 0

                    curr_player = self.player_name[round_order[round_index].name]
                    
            if(winner == -1):
                winner = self.check_winner()
            
                
            '''
            @TODO distribute winnings to winners, have more nuanced tie handling
            '''
            num_winner = len(winner)
            win_amt = self.pot/num_winner
            for i in range(num_winner):
                if(i>0):
                    p("and")
                p(f"Winner is {round_order[winner[i]].name}, Winning Amount is ${self.pot}", file=sys.stderr)
                self.players[self.player_name[round_order[winner[i]].name]].money += win_amt
            self.show_players()
            self.set_next_round()

        p("Not enough players", file=sys.stderr)

    def set_next_round(self):
        global gthread_dict
        while self.discard_pile:                            #Putting discard cards back in deck
            self.deck.pile.append(self.discard_pile.pop())

        while self.hole_cards:                              #Putting community cards back in deck
            self.deck.pile.append(self.hole_cards.pop())

        for i in self.players:
            i.curr_bet = 0
            i.game_bet = 0
            if i.cards:
                self.deck.pile.append(i.cards.pop())
                self.deck.pile.append(i.cards.pop())
            i.cards = []

        self.sb = (self.sb + 1) % self.num_players          #Rotating Small and Big Blind
        self.bb = (self.sb + 1) % self.num_players

        self.round_bet = 0
        self.pot = 0

        subtract_players = 0
        for i in range(self.num_players-1,-1,-1):
            if(self.players[i].money <= 0):
                #self.player_name.pop(self.players[i].name)
                self.player_address.pop(self.players[i].name)
                self.players.pop(i)
                subtract_players += 1
        
        self.num_players -= subtract_players

        self.player_name = dict()
        for i in range(self.num_players):
            self.player_name[self.players[i].name] = i 
        gthread_dict = self.player_address

    def distribute_cards(self):
        for i in self.players:
            i.cards.append(self.deck.pile.pop())
            i.cards.append(self.deck.pile.pop())

    def check_winner(self, round_players):
        winner = []
        max_hand = 0
        for i in round_players:
            hand_val = winningHand.checker(self.community+i.pile)
            if(hand_val == max_hand):
                winner.append(self.player_name[i.name])
            elif(hand_val > max_hand):
                max_hand = hand_val
                winner = [self.player_name[i.name]]

    def isPlaying(self, name):
        if name in self.player_name:
            return True
        return False

    def show_players(self):
        p(f"Pot Total".ljust(11)+f"- ${self.pot}",file=sys.stderr)
        for i in self.players:
            p(i.__str__(),file=sys.stderr)
        p("",file=sys.stderr)

    def show_hole_cards(self,round):                        # round (0 = pre-flop, 1 = flop, 2 = turn, 3 = river)
        p("Cards in the hole ",end="",file=sys.stderr)
        if(round == 0):
            p("(Pre-Flop)",file=sys.stderr)
        elif(round == 1):
            p("(Flop)",file=sys.stderr)
        elif(round == 2):
            p("(Turn)",file=sys.stderr)
        elif(round == 3):
            p("(River)",file=sys.stderr)    
        
        if(round == 0):
            for i in range(5):
                p(f"X".ljust(15),end="",file=sys.stderr)
        else:
            for i in range(5):
                if(i < 2+round):
                    p(f"{self.hole_cards[i]}".ljust(15),end="",file=sys.stderr)
                else:
                    p(f"X".ljust(15),end="",file=sys.stderr)
        
        p("\n",file=sys.stderr)

def p(string,end='\n',file=sys.stderr):
    print(string,end=end,file=sys.stderr)

def thread_receive(name):
    return gthread_dict[name][0].recv(1024).decode('UTF-8')

def thread_send(name, data):
    gthread_dict[name][0].send(str.encode(str(data)))

def thread_sendtoall(string):
    for i in gthread_dict:
        i[0].send(str.encode(str(string)))  
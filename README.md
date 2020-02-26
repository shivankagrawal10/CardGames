Purpose of this folder is to expirement with making the card game BS, initially this will be a person to person game, next step is to make this a host and server game, eventually I want to make this game automated through machine learning (Reinforcement Learning)

The Card.py file makes a deck of cards, it has a deck class that shuffles cards in two different ways. The shuffle algorithms are breakshuffle and riffleshuffle, these replicate the shuffling techniques used in real life. The riffle shuffle simulates spliting the deck in half and dropping intervals of random number of cards per deck. The breakshuffle takes a section of the deck from the middle and places it on top.

cardtester.py file instantiates 2 decks and measures the randomness of decks based on each of the shuffles. This file visualizes the randomness.

Random Measure.py aims to put a number on the randomness of the cards after shuffling. I analyze this from two weighted averages: how close to numerical order the cards are in (1,2,3 ...) or how close together similar numbers are (1,1,1,1)

Random Grapher.py - graphs the weighted randomness of the cards after calculating from the randommeasure code

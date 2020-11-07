
''' Attempt to build a Card Game in Python starting with GO FISH '''

import itertools
import random

suits = ['spade', 'club', 'hearts', 'diamonds']

cards = ['ace', 'king', 'queen', 'jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']

deck = list(itertools.product(suits, cards))

draw = itertools.count()

players = [[], []]
player_score = [0, 0]

class GoFish:

    def __init__(self, deck, cards):
        self.deck = deck
        self.cards = cards

    def match(player, card):
        x=0
        while x < len(players[player]):
            if card == players[player][x][1]:
                players[player].remove(players[player][x])
                player_score[player] += 1
            x+=1

    def check_pair(player):
        for i in cards:
            z=0
            for x in list(zip(*players[player]))[1]:
                if i == x:
                    z+=1
                if z == 4:
                    GoFish.match(player, i)

    def shuffle():
        random.shuffle(deck)

    def deal():
        for i in range(0,len(players)):
            x = 0
            while x < 7:
                players[i].append(deck[next(draw)])
                x+=1

    def fish(player):
        player.append(deck[next(draw)])
        pass

    def player_turn():
        choice = input("Ask For a card you would like to Steal --> ")
        x=0
        y = len(players[0])
        while x < len(players[1]):
            if str(choice) == str(players[1][x][1]):
                players[0].append(players[1][x])
                players[1].remove(players[1][x])
            x+=1
            if x == len(players[1]) and len(players[0]) == y:
                print("GO FISH")
                GoFish.fish(players[0])

    def computer_turn():
        choice = cards[random.randint(0, 12)]
        x=0
        y = len(players[1])
        while x < len(players[0]):
            if str(choice) == str(players[0][x][1]):
                players[1].append(players[0][x])
                players[0].remove(players[0][x])
            x+=1
            if x == len(players[0]) and len(players[1]) == y:
                print("Go Fish")
                GoFish.fish(players[1])
        pass



def play_gofish():
    GoFish.shuffle()
    GoFish.deal()
    while next(draw) < 51:
        print("Your Cards")
        print(players[0])
        print("Your Turn")
        GoFish.player_turn()
        GoFish.check_pair(0)
        print("Computers Turn")
        GoFish.computer_turn()
        GoFish.check_pair(1)
    print("Computer Hand")
    print(players[1])
    print("Player Score = {}".format(player_score[0]))
    print("Computer Score = {}".format(player_score[1]))




play_gofish()
# Adding this to make sure i still know what i am doing

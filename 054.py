"""
Created on 4/23/14 9:46 PM

@author: aaditya prakash

"""

import utilities as u
import time
import EXTUtilities as ex

problem_number = '054'

problem_statement = """
From the given poker.txt which contains 10 hands of a playing card, first five of player 1 and last 5 of player 2
Which player wins most hands
"""

def Hand_Value(p):
    """
    Returns the Value of the hand 1== High Card and 10 for Royal Flush
    """


    rank = []
    suite = []
    for card in p:
        if(len(card)<=2):
            rank.append(card[0])
            suite.append(card[1])
        else:
            rank.append(card[0]+card[1])
            suite.append(card[2])



    IsFlush = len(set(suite))==1
    srank = sorted(map(int, rank))
    IsStraight = int(srank[0])+4==int(srank[1])+3==int(srank[2])+2==int(srank[3])+1==int(srank[4])
    CardsInOrder = sorted(map(int, rank), reverse=True)



    #10 Check for Royal Flush
    if IsFlush and IsStraight and rank[0]=='10':
        #print('Royal Flush', p)
        return 10, CardsInOrder

    #9 Straight Flush
    if IsFlush and IsStraight:
        #print('Straight Flush', p)
        return 9, CardsInOrder


    NumUniqueCards = len(set(rank))
    DuplicatedCards = ex.list_duplicates(rank)
    NumRepeatedCards = len(DuplicatedCards)


    #8 Four of a Kind
    if NumUniqueCards ==2 and NumRepeatedCards == 1:
        #print('Four of a Kind', p, DuplicatedCards)
        return 8, DuplicatedCards

    #7 Full House
    if NumUniqueCards == 2 and NumRepeatedCards == 2:
        ReArrangedCards = DuplicatedCards if rank.count(DuplicatedCards[0]) == 3 else DuplicatedCards[::-1]
        #print('Full House', p, ReArrangedCards)
        return 7, ReArrangedCards

    #6 Flush
    if IsFlush:
        #print('Flush', p, CardsInOrder)
        return 6, CardsInOrder

    #5 Straight
    if IsStraight:
        #print('Straight', p, CardsInOrder)
        return 5, CardsInOrder

    #4 Three of a Kind
    if NumUniqueCards == 3 and NumRepeatedCards == 1:
        ReArrangedCards = []
        RepeatedRank = DuplicatedCards[0]
        ReArrangedCards.append(int(RepeatedRank))
        while RepeatedRank in rank:
            rank.remove(RepeatedRank)
        ReArrangedCards += sorted(map(int, rank), reverse=True)

        #print('Three of a Kind', p, ReArrangedCards)
        return 4, ReArrangedCards

    #3 Two pairs
    if NumUniqueCards == 3 and NumRepeatedCards == 2:
        ReArrangedCards = []
        Pair1 = max(DuplicatedCards[0] , DuplicatedCards[1])
        Pair2 = min(DuplicatedCards[0] , DuplicatedCards[1])
        ReArrangedCards.append(int(Pair1))
        ReArrangedCards.append(int(Pair2))
        while Pair1 in rank:
            rank.remove(Pair1)
        while Pair2 in rank:
            rank.remove(Pair2)
        ReArrangedCards += sorted(map(int, rank), reverse=True)


        #print('Two Pair', p, DuplicatedCards, CardsInOrder)
        return 3, ReArrangedCards

    #2 One Pair
    if NumUniqueCards == 4 and NumRepeatedCards == 1:
        ReArrangedCards = []
        RepeatedRank = DuplicatedCards[0]
        ReArrangedCards.append(int(RepeatedRank))
        while RepeatedRank in rank:
            rank.remove(RepeatedRank)
        ReArrangedCards += sorted(map(int, rank), reverse=True)


        #print('One Pair', p, DuplicatedCards)
        return 2, ReArrangedCards

    #1 Highest Value
    else:
        #print('Highest Value', p, CardsInOrder)
        return 1, CardsInOrder





def Poker_Strategy(p1, p2):
    """
    Given the poker hands as two lists, p1 and p2, returns 1 if player 1 wins else 0
    """


    val1, lCards1 = Hand_Value(p1)
    val2, lCards2 = Hand_Value(p2)

    #print(val1, lCards1)
    #print(val2, lCards2)
    if val1 > val2: return 1
    elif val1 < val2: return 0
    else:
        #if(val1>=5): #print("DANGER")
        #print("yolo")
        # this is the case where the value of hand might be same
        for i in range(len(lCards1)):
            if(lCards1[i]==lCards2[i]): continue
            elif(lCards1[i]>lCards2[i]): return 1
            else: return 0

        # if val1 == 10:
        #     #print("Cannot happened, contract Breached")
        #     return 0
        # elif val1 == 9:
        #     for i in range(len(lCards1)):
        #         if(lCards1[i]==lCards2[i]): continue
        #         elif(lCards1[i]>lCards2[i]): return 1
        #         else: return 0


def Poker_Hands():
    """
    Given the filename, opens and plays poker with the hands with each line as one game,
    returns total wins of each player
    """


    # s1 = '5H 5C 6S 7S KD 2C 3S 8S 8D TD'
    # s2 = '5D 8C 9S JS AC 2C 5C 7D 8S QH'
    # s3 = '2D 9C AS AH AC 3D 6D 7D TD QD'
    # s4 = '4D 6S 9H QH QC 3D 6D 7H QD QS'
    # s5 = '2H 2D 4C 4D 4S 3C 3D 3S 9S 9D'
    #
    # sf = '9D TC JS QH KC 3D 6D 7D TD QD'
    # s3K = '9D 9C 9S QH KC 3D 6D 7D TD QD'
    # sRF = 'TH JH QH KH AH 9H TH JH QH KH'

    player1Count = 0
    fIn = open('poker.txt', 'r')
    totalHandsCount=0
    for line in fIn:
        #print(line.rstrip())
        s = line.rstrip()
        v = 10
        for l in 'TJQKA':
            s = s.replace(l, str(v))
            v += 1
        ss = s.split(' ')
        p1, p2 = ss[:5], ss[5:]
        res = Poker_Strategy(p1, p2)
        totalHandsCount += 1
        player1Count += res
        ##print(str(res) + ' ' + str(player1Count) + ' ' + str(totalHandsCount) + '\n')
    return player1Count


timeStart = time.clock()
print(Poker_Hands())
print('Time (sec):' + str(time.clock() - timeStart))
answer = '376'



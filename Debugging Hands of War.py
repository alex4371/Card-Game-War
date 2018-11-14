#War project - Debugging any basic errors that occur
#By: alex4371
#This program was written to solve any errors that a specific dealing of cards has.
#Created: September 6, 2018
#Running on :Python 3.6.3
import random
def WarGame():
    '''
    Copy the Player hand into hand1 and the Computer hand into hand2 orders from the error message.
    
    If there is a presented order from a random order game, input it here as well.
    '''
    hand1 = [6, 2, 12, 5, 3, 14, 8, 8, 6, 10, 12, 5, 11, 6, 2, 11, 5, 9, 7, 7, 9, 5, 10, 4, 11, 10, 13]
    hand2 = [12, 2, 4, 11, 3, 13, 1, 8, 8, 13, 7, 4, 1, 1, 1, 14, 9, 9, 13, 3, 3, 2, 4, 12, 6, 7, 10]
    orderInput = 0x100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    #Use a 1 followed by a bunch of 0's for WF and F's for LF 
    roundNum = 0
    print("Begining Game")
    print("Shuffling cards")
    print("========================================Hand", roundNum,"========================================")
    print("Player Hand:", hand1)
    print("Computer Hand:", hand2)
    orderBin = bin(orderInput)
    print(orderBin)
    print(orderInput)
    print(bin(orderInput))
    
    while len(hand1) != 0 and len(hand2) !=0:
        
        order = int(orderBin[roundNum+3])
        
        if hand1[0] > hand2[0]:
            if order == 0:
                hand1.append(hand1.pop(0))
                hand1.append(hand2.pop(0))
            elif order == 1:
                hand1.append(hand2.pop(0))
                hand1.append(hand1.pop(0))
        elif hand2[0] > hand1[0]:
            if order == 0:
                hand2.append(hand2.pop(0))
                hand2.append(hand1.pop(0))
            elif order == 1:
                hand2.append(hand1.pop(0))
                hand2.append(hand2.pop(0))

#####################################War Analysis#####################################
            
        elif hand1[0] == hand2[0]:
            print("War")
            warComplete = False
            warStep = 4
            warStep1 = 0
            warStep2 = 0
            while warComplete == False:
                
###################################### If a hand is empty

                if len(hand1) == 1:
                    hand2.append(hand1.pop(0))
                    warComplete = True
                elif len(hand2) == 1:
                    hand1.append(hand2.pop(0))
                    warComplete = True

###################################### If a hand is shorter than 4
                    
                elif warStep >= len(hand1):
                    warStep1 = len(hand1)-1
                elif warStep >= len(hand2):
                    warStep2 = len(hand2)-1

###################################### If hand1 wins war
                        
                elif hand1[warStep] > hand2[warStep]:
                    for i in range(0, warStep+1):
                        if order == 0:
                            hand1.append(hand1.pop(0))
                            hand1.append(hand2.pop(0))
                        elif order == 1:
                            hand1.append(hand2.pop(0))
                            hand1.append(hand1.pop(0)) 
                    warComplete = True

###################################### If hand2 wins war
                    
                elif hand2[warStep] > hand1[warStep]:
                    for i in range(0, warStep+1):
                        if order == 0:
                            hand2.append(hand2.pop(0))
                            hand2.append(hand1.pop(0))
                        elif order == 1:
                            hand2.append(hand1.pop(0))
                            hand2.append(hand2.pop(0))
                    warComplete = True

###################################### If the war continues
                    
                elif hand2[warStep] == hand2[warStep]:
                    print("Double War")
                    warStep += 4
                    
##################################### If hand1 is shorter than 4

                if warStep1 != 0:
                    if hand1[warStep1] > hand2[warStep]:
                        for i in range(0, warStep +1):
                            hand1.append(hand2.pop(0))
                        warComplete = True
                        
                    elif hand1[warStep1] < hand2[warStep]:
                        for i in range(0, len(hand1)):
                            hand2.append(hand1.pop(0))
                        warComplete = True
                        
                    elif hand1[warStep1] == hand2[warStep]:
                        print("Double War")
                        warStep += 4
                        
###################################### If hand2 is shorter than 4
                        
                elif warStep2 != 0:
                    if hand2[warStep2] > hand1[warStep]:
                        for i in range(0, warStep +1):
                            hand1.append(hand1.pop(0))
                        warComplete = True
                            
                    elif hand2[warStep2] < hand1[warStep]:
                        for i in range(0, len(hand2)):
                            hand1.append(hand2.pop(0))
                        warComplete = True
                    elif hand2[warStep2] == hand1[warStep]:
                        print("Double War")
                        warStep += 4
###################################################################                                       

                    
        roundNum = roundNum + 1
        
        print("========================================Hand", roundNum,"========================================")
        print("Player Hand:", hand1)
        print("Computer Hand:", hand2)
        if order is 0:
            print("Winner First Hand")
        elif order is 1:
            print("Loser First Hand")
                
    print("Game End after", roundNum, "rounds")
    print("Binary order in game", orderBin)
    print("Hexadecimal order in game", hex(orderInput))
    if len(hand1) != 0:
        print("Hand1 Wins")
    elif len(hand2) != 0:
        print("Hand2 Wins")

##########################################################################################


WarGame()
        

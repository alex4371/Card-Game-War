#War project - This file has the three basic types of games and thier possible jocker values in one
#Alex Pavlik
#This program was written to collect data on the length of games of war and their connection to the frequency of wars appearing
#Created: August 2, 2018
#Running on :Python 3.6.3
import random


#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#-------------------------------Winner First Function----------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
def WarGameWinnerFirst(jokers):
    try:
        #Variable clearing/definition
        global hand1Saved, hand2Saved, warSum
        deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,14,14,14,14]
        hand1 = []
        hand2 = []
        hand1Saved = []
        hand2Saved = []
        hand1Sum = 0
        hand2Sum = 0
        warSum = [0,0,0,0,0,0,0,0]
        playerWins = False
        roundNum = 0
        
        #Taking out the necessay number of jockers
        for i in range(-jokers + 4):
            deck.pop(-1)
            
        #Shuffling the deck
        while len(deck) > 0:
            hand1.append(deck.pop(random.randint(0,len(deck)-1)))
            hand2.append(deck.pop(random.randint(0,len(deck)-1)))

        #Saving the order of the shuffle
        hand1Saved = hand1[:]
        hand2Saved = hand2[:]

        #Saving the sum of the starting deal as another data point
        hand1Sum = sum(hand1)
        hand2Sum = sum(hand2)
            
        #This code plays most of the games
        while len(hand1) != 0 and len(hand2) !=0:
            if hand1[0] > hand2[0]:
                hand1.append(hand1.pop(0))
                hand1.append(hand2.pop(0))
            elif hand2[0] > hand1[0]:
                hand2.append(hand2.pop(0))
                hand2.append(hand1.pop(0))

############################# War Analysis #############################
                
            elif hand1[0] == hand2[0]:
                warComplete = False
                warStep = 4
                warStep1 = 0
                warStep2 = 0
                while warComplete == False:
                    warSaveSlot = int((warStep/4) - 1)
                
###################################### If a hand is empty

                    if len(hand1) == 1:
                        hand2.append(hand1.pop(0))
                        warComplete = True
                        warSum[0] += 1
                        
                    elif len(hand2) == 1:
                        hand1.append(hand2.pop(0))
                        warComplete = True
                        warSum[0] += 1

###################################### If a hand is shorter than 4
                    
                    elif warStep >= len(hand1):
                        warStep1 = len(hand1)-1
                    elif warStep >= len(hand2):
                        warStep2 = len(hand2)-1

###################################### If hand1 wins war
                        
                    elif hand1[warStep] > hand2[warStep]:
                        for i in range(0, warStep+1):
                            hand1.append(hand1.pop(0))
                            hand1.append(hand2.pop(0)) 
                        warComplete = True
                        warSum[warSaveSlot] += 1

###################################### If hand2 wins war
                    
                    elif hand2[warStep] > hand1[warStep]:
                        for i in range(0, warStep+1):
                            hand2.append(hand2.pop(0))
                            hand2.append(hand1.pop(0))
                        warComplete = True
                        warSum[warSaveSlot] += 1

###################################### If the war continues
                    
                    elif hand2[warStep] == hand2[warStep]:
                        warStep += 4

###################################### If hand1 is shorter than 4

                    if warStep1 != 0:
                        if hand1[warStep1] > hand2[warStep]:
                            for i in range(0, warStep +1):
                                hand1.append(hand2.pop(0))
                            warComplete = True
                            warSum[warSaveSlot] += 1
                            
                        elif hand1[warStep1] < hand2[warStep]:
                            for i in range(0, len(hand1)):
                                hand2.append(hand1.pop(0))
                            warComplete = True
                            warSum[warSaveSlot] += 1
                            
                        elif hand1[warStep1] == hand2[warStep]:
                            warStep += 4
                            
###################################### If hand2 is shorter than 4
                        
                    elif warStep2 != 0:
                        if hand2[warStep2] > hand1[warStep]:
                            for i in range(0, warStep +1):
                                hand1.append(hand1.pop(0))
                            warComplete = True
                            warSum[warSaveSlot] += 1
                                
                        elif hand2[warStep2] < hand1[warStep]:
                            for i in range(0, len(hand2)):
                                hand1.append(hand2.pop(0))
                            warComplete = True
                            warSum[warSaveSlot] += 1
                            
                        elif hand2[warStep2] == hand1[warStep]:
                            warStep += 4

############################################################################
                                        
            #Making sure a game that cycles wont crash the program                           
            roundNum = roundNum + 1
            if roundNum > 10000:
                roundNum = 0
                warComplete = True

        if len(hand1) != 0:
            playerWins = True
        elif len(hand2) != 0:
            playerWins = False
            
        return hand1Saved, hand2Saved, roundNum, playerWins, hand1Sum, hand2Sum, warSum
    
    except:
        print("An Error Occured, Please Solve")
        print("Player Hand:", hand1Saved)
        print("Computer Hand:", hand2Saved)
        print("Number of Wars:", warSum)


#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#-------------------------------Loser First Function-----------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
def WarGameLoserFirst(jokers):
    try:
        #Variable clearing/definition
        global hand1Saved, hand2Saved, warSum
        deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,14,14,14,14]
        hand1 = []
        hand2 = []
        hand1Saved = []
        hand2Saved = []
        hand1Sum = 0
        hand2Sum = 0
        warSum = [0,0,0,0,0,0,0,0]
        playerWins = False
        roundNum = 0

        #Taking out the necessay number of jockers
        for i in range(-jokers + 4):
            deck.pop(-1)
            
        #Shuffling the deck
        while len(deck) > 0:
            hand1.append(deck.pop(random.randint(0,len(deck)-1)))
            hand2.append(deck.pop(random.randint(0,len(deck)-1)))

        #Saving the order of the shuffle
        hand1Saved = hand1[:]
        hand2Saved = hand2[:]
        
        #Saving the sum of the starting deal as another data point
        hand1Sum = sum(hand1)
        hand2Sum = sum(hand2)

        #This code plays most of the games
        while len(hand1) != 0 and len(hand2) !=0:
            if hand1[0] > hand2[0]:
                hand1.append(hand2.pop(0))
                hand1.append(hand1.pop(0))
            elif hand2[0] > hand1[0]:
                hand2.append(hand1.pop(0))
                hand2.append(hand2.pop(0))

############################# War Analysis #############################
                
            elif hand1[0] == hand2[0]:
                warComplete = False
                warStep = 4
                warStep1 = 0
                warStep2 = 0
                while warComplete == False:
                    warSaveSlot = int((warStep/4) - 1)
                
###################################### If a hand is empty

                    if len(hand1) == 1:
                        hand2.append(hand1.pop(0))
                        warComplete = True
                        warSum[0] += 1
                        
                    elif len(hand2) == 1:
                        hand1.append(hand2.pop(0))
                        warComplete = True
                        warSum[0] += 1

###################################### If a hand is shorter than 4
                    
                    elif warStep >= len(hand1):
                        warStep1 = len(hand1)-1
                    elif warStep >= len(hand2):
                        warStep2 = len(hand2)-1

###################################### If hand1 wins war
                        
                    elif hand1[warStep] > hand2[warStep]:
                        for i in range(0, warStep+1):
                            hand1.append(hand2.pop(0))
                            hand1.append(hand1.pop(0)) 
                        warComplete = True
                        warSum[warSaveSlot] += 1

###################################### If hand2 wins war
                    
                    elif hand2[warStep] > hand1[warStep]:
                        for i in range(0, warStep+1):
                            hand2.append(hand1.pop(0))
                            hand2.append(hand2.pop(0))
                        warComplete = True
                        warSum[warSaveSlot] += 1

###################################### If the war continues
                    
                    elif hand2[warStep] == hand2[warStep]:
                        warStep += 4

###################################### If hand1 is shorter than warstep

                    if warStep1 != 0:
                        if hand1[warStep1] > hand2[warStep]:
                            for i in range(0, warStep +1):
                                hand1.append(hand2.pop(0))
                            warComplete = True
                            warSum[warSaveSlot] += 1
                            
                        elif hand1[warStep1] < hand2[warStep]:
                            for i in range(0, len(hand1)):
                                hand2.append(hand1.pop(0))
                            warComplete = True
                            warSum[warSaveSlot] += 1
                            
                        elif hand1[warStep1] == hand2[warStep]:
                            warStep += 4
                            
###################################### If hand2 is shorter than 4
                        
                    elif warStep2 != 0:
                        if hand2[warStep2] > hand1[warStep]:
                            for i in range(0, warStep +1):
                                hand1.append(hand1.pop(0))
                            warComplete = True
                            warSum[warSaveSlot] += 1
                                
                        elif hand2[warStep2] < hand1[warStep]:
                            for i in range(0, len(hand2)):
                                hand1.append(hand2.pop(0))
                            warComplete = True
                            warSum[warSaveSlot] += 1
                            
                        elif hand2[warStep2] == hand1[warStep]:
                            warStep += 4

############################################################################

            #Making sure a game that cycles wont crash the program                              
            roundNum = roundNum + 1
            if roundNum > 10000:
                roundNum = 0
                warComplete = True
                    
        if len(hand1) != 0:
            playerWins = True
        elif len(hand2) != 0:
            playerWins = False
            
        return hand1Saved, hand2Saved, roundNum, playerWins, hand1Sum, hand2Sum, warSum
    
    except:
        print("An Error Occured, Please Solve")
        print("Player Hand:", hand1Saved)
        print("Computer Hand:", hand2Saved)
        print("Number of Wars:", warSum)



#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#-------------------------------Random Order Function----------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
def WarGameRandom(jokers):
    try:
        #Variable clearing/definition
        global hand1Saved, hand2Saved, warSum
        deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,14,14,14,14]
        hand1 = []
        hand2 = []
        hand1Saved = []
        hand2Saved = []
        hand1Sum = 0
        hand2Sum = 0
        warSum = [0,0,0,0,0,0,0,0]
        playerWins = False
        roundNum = 0
        order = '1'

        #Taking out the necessay number of jockers
        for i in range(-jokers + 4):
            deck.pop(-1)

        #Shuffling the deck
        while len(deck) > 0:
            hand1.append(deck.pop(random.randint(0,len(deck)-1)))
            hand2.append(deck.pop(random.randint(0,len(deck)-1)))

        #Saving the order of the shuffle
        hand1Saved = hand1[:]
        hand2Saved = hand2[:]
        
        #Saving the sum of the starting deal as another data point
        hand1Sum = sum(hand1)
        hand2Sum = sum(hand2)

        #Starting this game
        while len(hand1) != 0 and len(hand2) !=0:

            #Choosing the random order for this hand (0 = WF, 1 = LF)
            rand = random.randint(0,1)
            order = order + str(rand)

            #Playing most hands
            if hand1[0] > hand2[0]:
                if rand == 0:
                    hand1.append(hand1.pop(0))
                    hand1.append(hand2.pop(0))
                elif rand == 1:
                    hand1.append(hand2.pop(0))
                    hand1.append(hand1.pop(0))
            elif hand2[0] > hand1[0]:
                if rand == 0:
                    hand2.append(hand2.pop(0))
                    hand2.append(hand1.pop(0))
                elif rand == 1:
                    hand2.append(hand1.pop(0))
                    hand2.append(hand2.pop(0))

############################# War Analysis #############################
                
            elif hand1[0] == hand2[0]:
                warComplete = False
                warStep = 4
                warStep1 = 0
                warStep2 = 0
                while warComplete == False:
                    warSaveSlot = int((warStep/4) - 1)
                    
###################################### If a hand has no other cards

                    if len(hand1) == 1:
                        hand2.append(hand1.pop(0))
                        warComplete = True
                        warSum[0] += 1
                    elif len(hand2) == 1:
                        hand1.append(hand2.pop(0))
                        warComplete = True
                        warSum[0] += 1

###################################### If a hand is shorter than 4
                    
                    elif warStep >= len(hand1):
                        warStep1 = len(hand1)-1
                    elif warStep >= len(hand2):
                        warStep2 = len(hand2)-1

###################################### If hand1 wins war
                        
                    elif hand1[warStep] > hand2[warStep]:
                        for i in range(0, warStep+1):
                            if rand == 0:
                                hand1.append(hand1.pop(0))
                                hand1.append(hand2.pop(0))
                            elif rand == 1:
                                hand1.append(hand2.pop(0))
                                hand1.append(hand1.pop(0)) 
                        warComplete = True
                        warSum[warSaveSlot] += 1

###################################### If hand2 wins war
                    
                    elif hand2[warStep] > hand1[warStep]:
                        for i in range(0, warStep+1):
                            if rand == 0:
                                hand2.append(hand2.pop(0))
                                hand2.append(hand1.pop(0))
                            elif rand ==1:
                                hand2.append(hand1.pop(0))
                                hand2.append(hand2.pop(0))
                        warComplete = True
                        warSum[warSaveSlot] += 1

###################################### If the war continues
                    
                    elif hand2[warStep] == hand2[warStep]:
                        warStep += 4

###################################### If hand1 is shorter than 4

                    if warStep1 != 0:
                        if hand1[warStep1] > hand2[warStep]:
                            for i in range(0, warStep +1):
                                hand1.append(hand2.pop(0))
                            warComplete = True
                            warSum[warSaveSlot] += 1
                            
                        elif hand1[warStep1] < hand2[warStep]:
                            for i in range(0, len(hand1)):
                                hand2.append(hand1.pop(0))
                            warComplete = True
                            warSum[warSaveSlot] += 1
                            
                        elif hand1[warStep1] == hand2[warStep]:
                            warStep += 4
                            
###################################### If hand2 is shorter than 4
                        
                    elif warStep2 != 0:
                        if hand2[warStep2] > hand1[warStep]:
                            for i in range(0, warStep +1):
                                hand1.append(hand1.pop(0))
                            warComplete = True
                            warSum[warSaveSlot] += 1
                            
                        elif hand2[warStep2] < hand1[warStep]:
                            for i in range(0, len(hand2)):
                                hand1.append(hand2.pop(0))
                            warComplete = True
                            warSum[warSaveSlot] += 1
                            
                        elif hand2[warStep2] == hand1[warStep]:
                            warStep += 4

############################################################################
                                        
            roundNum = roundNum + 1

            #No need to make sure a game doesn't cycle becasue of "On finiteness in the card game war" by Evgeny Lakshtanov, and Vera Roshchina
                
        if len(hand1) != 0:
            playerWins = True
        elif len(hand2) != 0:
            playerWins = False
       
        #Converting the order string into hexidecimal so it will save memory space.
        orderSaved = str(hex(int(order, 2)))
        return hand1Saved, hand2Saved, roundNum, playerWins, orderSaved, hand1Sum, hand2Sum, warSum
    
    except:
        print("An Error Occured, Please Solve")
        print("Player Hand:", hand1Saved)
        print("Computer Hand:", hand2Saved)
        print("Number of Wars:", warSum)

        
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#-------------------------------Core Control Code--------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

while True:
    try:
        mode = input('For Winner First game enter "W", For Loser First game enter "L", For Random Order game enter "R", To exit enter "C":')
        if mode is 'C': #Allowing you to escape from the program
            break
        count = input('Number of games:')
        jokers = input('Number of Jockers(0,2,4):')
        fileName = input('Name of the file to save to(eg. data.txt):')
        file = open(fileName, "a")

        try:
            count = int(count)
            jokersNum = int(jokers)
        except:
            print("Please enter a valid number")
            continue
        ############################Winner first###########################

        if mode is 'W':
            for i in range(count):
                hand1Save, hand2Save, rounds, whoWins, hand1Sum, hand2Sum, warSum = WarGameWinnerFirst(jokersNum)
                #Reformatting arrays to work with the delimiter
                s = str(hand1Save)
                s1 = s.replace("]","")
                s = str(hand2Save)
                s2 = s.replace("]","")
                s = str(warSum)
                s3 = s.replace(']','')
                s3 = s3.replace(',','[')

                file.write('\n')
                file.write("WF")
                file.write(str(jokersNum))
                file.write("[")
                file.write(str(int(whoWins)))
                file.write("[")
                file.write(str(hand1Sum))
                file.write("[")
                file.write(str(hand2Sum))
                file.write("[")
                file.write(str(rounds))
                file.write(s1)
                file.write(s2)
                file.write(s3)
                
            #Data save order (Game type, Winner boolean, sum of hand 1, sum of hand 2, number of wars, number of rounds, starting shuffle of hand 1, starting shuffle of hand 2, number of wars)
            
        ############################Loser first###########################

        elif mode is 'L':
            for i in range(count):
                hand1Save, hand2Save, rounds, whoWins, hand1Sum, hand2Sum, warSum = WarGameWinnerFirst(jokersNum)
                #Reformatting arrays to work with the delimiter
                s = str(hand1Save)
                s1 = s.replace("]","")
                s = str(hand2Save)
                s2 = s.replace("]","")
                s = str(warSum)
                s3 = s.replace(']','')
                s3 = s3.replace(',','[')

                file.write('\n')
                file.write("LF")
                file.write(str(jokersNum))
                file.write("[")
                file.write(str(int(whoWins)))
                file.write("[")
                file.write(str(hand1Sum))
                file.write("[")
                file.write(str(hand2Sum))
                file.write("[")
                file.write(str(rounds))
                file.write(s1)
                file.write(s2)
                file.write(s3)

            #Data save order (Game type, Winner boolean, sum of hand 1, sum of hand 2, number of rounds, starting shuffle of hand 1, starting shuffle of hand 2, number of wars)

        ############################Random first###########################

        elif mode is 'R':
            for i in range(count):
                hand1Save, hand2Save, rounds, whoWins, hand1Sum, hand2Sum, warSum = WarGameWinnerFirst(jokersNum)
                #Reformatting arrays to work with the delimiter
                s = str(hand1Save)
                s1 = s.replace("]","")
                s = str(hand2Save)
                s2 = s.replace("]","")
                s = str(warSum)
                s3 = s.replace(']','')
                s3 = s3.replace(',','[')

                file.write('\n')
                file.write("RF")
                file.write(str(jokersNum))
                file.write("[")
                file.write(str(int(whoWins)))
                file.write("[")
                file.write(str(hand1Sum))
                file.write("[")
                file.write(str(hand2Sum))
                file.write("[")
                file.write(str(rounds))
                file.write(s1)
                file.write(s2)
                file.write(s3)
                file.write("[")
                file.write(orderSaved)

            #Data save order (Game type, Winner boolean, sum of hand 1, sum of hand 2, number of rounds, starting shuffle of hand 1, starting shuffle of hand 2, number of wars, order of WF/LF)

        ############################To prevent an error############################
        else:
            print('Please enter a valid type of game or enter "C" to cancel')
            
        file.close()
    except:
        print("An error occured outside of a game")
        print(hand1Saved)
        print(hand2Saved)
        print(warSum)
        continue



'''
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
-------------------------------Program Notes------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
This is still a changing project and will be editited often.

This data is designed to be entered into a database with '[' being the delimiting character.

If any game is saved with a 0 rounds, that means it went to 10,000 rounds and was forced to stop.

There are catches in to keep any errors from causing a fatal crash of the program.

The program generally takes 10 minutes to run 1,000,000 games.

There is some optimization that can be done by combining the three functions into one, but for debuggin they were left seperate.




'''

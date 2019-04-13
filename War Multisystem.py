#War project - This file has the nine basic types of games in one
#By: Alex Pavlik
#GitHub: alex4371 – A Statistical Analysis of the Card Game War
#This program was written to collect data on the card game War
#Created: August 2, 2018
#Last Modified: December 2, 2018
#Running on :Python 3.6.3


import random


#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#-------------------------------Higher First Function----------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
def WarGameHigherFirst(jokers):
    try:
        #Variable clearing/definition
        deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,
                1,2,3,4,5,6,7,8,9,10,11,12,13,
                1,2,3,4,5,6,7,8,9,10,11,12,13,
                1,2,3,4,5,6,7,8,9,10,11,12,13,
                14,14,14,14]
        hand1 = []
        hand2 = []
        hand1Saved = []
        hand2Saved = []
        hand1Sum = 0
        hand2Sum = 0
        warSum = [0,0,0,0,0,0,0,0]
        playerWins = False
        roundNum = 0
        
        #Taking out the necessary number of jockers
        for i in range (-jokers + 4):
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
            
        #This code plays every hand that is not a war
        while len(hand1) != 0 and len(hand2) !=0:
            if hand1[0] > hand2[0]:
                hand1.append(hand1.pop(0))
                hand1.append(hand2.pop(0))
            elif hand2[0] > hand1[0]:
                hand2.append(hand2.pop(0))
                hand2.append(hand1.pop(0))



############################# War Handling #############################
                
            elif hand1[0] == hand2[0]:
                warComplete = False
                warStep = 4         #Variable to track how many cards to skip

                warStep1 = 0        #Variables used if one deck is too short
                warStep2 = 0        #to continue with a normal war
                while warComplete == False:
                    
####################This variable keeps the information about
####################the war being a single, double, triple, etc. war
                    warSaveSlot = int((warStep/4) - 1)
                    
####################If a hand is empty except for the card that has been compared

                    if len(hand1) == 1:
                        hand2.append(hand1.pop(0))
                        warComplete = True
                        warSum[0] += 1
                    elif len(hand2) == 1:
                        hand1.append(hand2.pop(0))
                        warComplete = True
                        warSum[0] += 1

####################If a hand is shorter than warstep
####################This prevents the program from
####################looking for a card that doesn’t exist
####################It needs to be this early to skip to 
####################the next "if" statement
                        
                    elif warStep >= len(hand1):
                        warStep1 = len(hand1)-1
                    elif warStep >= len(hand2):
                        warStep2 = len(hand2)-1

####################If hand1 wins the war
                        
                    elif hand1[warStep] > hand2[warStep]:
                        for i in range (0, warStep+1):
                            hand1.append(hand1.pop(0))
                            hand1.append(hand2.pop(0)) 
                        warComplete = True
                        warSum[warSaveSlot] += 1

####################If hand2 wins war
                    
                    elif hand2[warStep] > hand1[warStep]:
                        for i in range (0, warStep+1):
                            hand2.append(hand2.pop(0))
                            hand2.append(hand1.pop(0))
                        warComplete = True
                        warSum[warSaveSlot] += 1

####################If the war is not resolved simply, skip 4 more cards 
                    
                    elif hand2[warStep] == hand2[warStep]:
                        warStep += 4





####################This code handles if one hand is shorter than 
####################warstep, but is not 1 card
                      
####################If hand1 is shorter than warstep

                    if warStep1 != 0:
                        if hand1[warStep1] > hand2[warStep]:
                            for i in range (0, warStep +1):
                                hand1.append(hand2.pop(0))
                            warComplete = True
                            warSum[warSaveSlot] += 1
                            
                        elif hand1[warStep1] < hand2[warStep]:
                            for i in range (0, len(hand1)):
                                hand2.append(hand1.pop(0))
                            warComplete = True
                            warSum[warSaveSlot] += 1

                        #If the war is still not resolved skip 4 more cards   
                        elif hand1[warStep1] == hand2[warStep]:
                            warStep += 4
                            
####################If hand2 is shorter than warstep
                        
                    elif warStep2 != 0:
                        if hand2[warStep2] > hand1[warStep]:
                            for i in range (0, warStep +1):
                                hand1.append(hand1.pop(0))
                            warComplete = True
                            warSum[warSaveSlot] += 1
                                
                        elif hand2[warStep2] < hand1[warStep]:
                            for i in range (0, len(hand2)):
                                hand1.append(hand2.pop(0))
                            warComplete = True
                            warSum[warSaveSlot] += 1

                        #If the war is still not resolved skip 4 more cards
                        elif hand2[warStep2] == hand1[warStep]:
                            warStep += 4

####################################End of War###################################
                                        
            #Making sure a game that cycles won’t crash the program
            roundNum = roundNum + 1
            if roundNum > 10000:
                roundNum = 0
                warComplete = True
                
########This runs when a game has finished
        if len(hand1) != 0:
            playerWins = True
        elif len(hand2) != 0:
            playerWins = False
            
        return hand1Saved, hand2Saved, roundNum, playerWins, hand1Sum, hand2Sum, warSum
    
    except:
        print("An Error Occurred, Please Solve")
        print("Player Hand:", hand1Saved)
        print("Computer Hand:", hand2Saved)
        print("Number of Wars:", warSum)
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#-------------------------------Loser First Function-----------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
def WarGameLowerFirst(jokers):
    try:
        #Variable clearing/definition
        deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,
                1,2,3,4,5,6,7,8,9,10,11,12,13,
                1,2,3,4,5,6,7,8,9,10,11,12,13,
                1,2,3,4,5,6,7,8,9,10,11,12,13,
                14,14,14,14]
        hand1 = []
        hand2 = []
        hand1Saved = []
        hand2Saved = []
        hand1Sum = 0
        hand2Sum = 0
        warSum = [0,0,0,0,0,0,0,0]
        playerWins = False
        roundNum = 0
        
        #Taking out the necessary number of jockers
        for i in range (-jokers + 4):
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
            
        #This code plays every hand that is not a war
        while len(hand1) != 0 and len(hand2) !=0:
            if hand1[0] > hand2[0]:
                hand1.append(hand2.pop(0))
                hand1.append(hand1.pop(0))
            elif hand2[0] > hand1[0]:
                hand2.append(hand1.pop(0))
                hand2.append(hand2.pop(0))

############################# War Handling #############################
                
            elif hand1[0] == hand2[0]:
                warComplete = False
                warStep = 4         #Variable to track how many cards to skip

                warStep1 = 0        #Variables used if one deck is too short
                warStep2 = 0        #to continue with a normal war
                while warComplete == False:
                    
####################This variable keeps the information about
####################the war being a single, double, triple, etc. war
                    warSaveSlot = int((warStep/4) - 1)
                    
####################If a hand is empty except for the card that has been compared

                    if len(hand1) == 1:
                        hand2.append(hand1.pop(0))
                        warComplete = True
                        warSum[0] += 1
                    elif len(hand2) == 1:
                        hand1.append(hand2.pop(0))
                        warComplete = True
                        warSum[0] += 1

####################If a hand is shorter than warstep
####################This prevents the program from
####################looking for a card that doesn’t exist
####################It needs to be this early to skip to 
####################the next "if" statement
                        
                    elif warStep >= len(hand1):
                        warStep1 = len(hand1)-1
                    elif warStep >= len(hand2):
                        warStep2 = len(hand2)-1

####################If hand1 wins the war
                        
                    elif hand1[warStep] > hand2[warStep]:
                        for i in range (0, warStep+1):
                            hand1.append(hand2.pop(0))
                            hand1.append(hand1.pop(0)) 
                        warComplete = True
                        warSum[warSaveSlot] += 1

####################If hand2 wins the war
                    
                    elif hand2[warStep] > hand1[warStep]:
                        for i in range (0, warStep+1):
                            hand2.append(hand1.pop(0))
                            hand2.append(hand2.pop(0))
                        warComplete = True
                        warSum[warSaveSlot] += 1

####################If the war is not resolved simply, skip 4 more cards 
                    
                    elif hand2[warStep] == hand2[warStep]:
                        warStep += 4

####################This code handles if one hand is shorter than 
####################warstep, but is not 1 card
                        
####################If hand1 is shorter than warstep

                    if warStep1 != 0:
                        if hand1[warStep1] > hand2[warStep]:
                            for i in range (0, warStep +1):
                                hand1.append(hand2.pop(0))
                            warComplete = True
                            warSum[warSaveSlot] += 1
                            
                        elif hand1[warStep1] < hand2[warStep]:
                            for i in range (0, len(hand1)):
                                hand2.append(hand1.pop(0))
                            warComplete = True
                            warSum[warSaveSlot] += 1

                        #If the war is still not resolved skip 4 more cards 
                        elif hand1[warStep1] == hand2[warStep]:
                            warStep += 4
                            
#################### If hand2 is shorter than warstep
                        
                    elif warStep2 != 0:
                        if hand2[warStep2] > hand1[warStep]:
                            for i in range (0, warStep +1):
                                hand1.append(hand1.pop(0))
                            warComplete = True
                            warSum[warSaveSlot] += 1
                                
                        elif hand2[warStep2] < hand1[warStep]:
                            for i in range (0, len(hand2)):
                                hand1.append(hand2.pop(0))
                            warComplete = True
                            warSum[warSaveSlot] += 1

                        #If the war is still not resolved skip 4 more cards 
                        elif hand2[warStep2] == hand1[warStep]:
                            warStep += 4

###################################End of War####################################

            #Making sure a game that cycles won’t crash the program
            roundNum = roundNum + 1
            if roundNum > 10000:
                roundNum = 0
                warComplete = True
                
########This runs when a game has finished
        if len(hand1) != 0:
            playerWins = True
        elif len(hand2) != 0:
            playerWins = False
            
        return hand1Saved, hand2Saved, roundNum, playerWins, hand1Sum, hand2Sum,
                warSum
    
    except:
        print("An Error Occurred, Please Solve")
        print("Player Hand:", hand1Saved)
        print("Computer Hand:", hand2Saved)
        print("Number of Wars:", warSum)
 
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#-------------------------------Random Order Function----------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
def WarGameRandomFirst(jokers):
    try:
        #Variable clearing/definition
        deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,
                1,2,3,4,5,6,7,8,9,10,11,12,13,
                1,2,3,4,5,6,7,8,9,10,11,12,13,
                1,2,3,4,5,6,7,8,9,10,11,12,13,
                14,14,14,14]
        hand1 = []
        hand2 = []
        hand1Saved = []
        hand2Saved = []
        hand1Sum = 0
        hand2Sum = 0
        warSum = [0,0,0,0,0,0,0,0]
        playerWins = False
        roundNum = 0
        
        #Taking out the necessary number of jockers
        for i in range (-jokers + 4):
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

            #This code plays every hand that is not a war
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

############################# War Handling #############################
                
            elif hand1[0] == hand2[0]:
                warComplete = False
                warStep = 4         #Variable to track how many cards to skip

                warStep1 = 0        #Variables used if one deck is too short
                warStep2 = 0        #to continue with a normal war
                while warComplete == False:
                    
####################This variable keeps the information about
####################the war being a single, double, triple, etc. war
                    warSaveSlot = int((warStep/4) - 1)
                    
####################If a hand is empty except for the card that has been compared

                    if len(hand1) == 1:
                        hand2.append(hand1.pop(0))
                        warComplete = True
                        warSum[0] += 1
                    elif len(hand2) == 1:
                        hand1.append(hand2.pop(0))
                        warComplete = True
                        warSum[0] += 1

####################If a hand is shorter than warstep
####################This prevents the program from
####################looking for a card that doesn’t exist
####################It needs to be this early to skip to 
####################the next "if" statement
                        
                    elif warStep >= len(hand1):
                        warStep1 = len(hand1)-1
                    elif warStep >= len(hand2):
                        warStep2 = len(hand2)-1

####################If hand1 wins the war
                        
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

####################If hand2 wins the war
                    
                    elif hand2[warStep] > hand1[warStep]:
                        for i in range (0, warStep+1):
                            if rand == 0:
                                hand2.append(hand2.pop(0))
                                hand2.append(hand1.pop(0))
                            elif rand ==1:
                                hand2.append(hand1.pop(0))
                                hand2.append(hand2.pop(0))
                        warComplete = True
                        warSum[warSaveSlot] += 1


####################If the war is not resolved simply, skip 4 more cards 
                    
                    elif hand2[warStep] == hand2[warStep]:
                        warStep += 4

####################This code handles if one hand is shorter than 
####################warstep, but is not 1 card

####################If hand1 is shorter than warstep
                        
                    if warStep1 != 0:
                        if hand1[warStep1] > hand2[warStep]:
                            for i in range (0, warStep +1):
                                hand1.append(hand2.pop(0))
                            warComplete = True
                            warSum[warSaveSlot] += 1
                            
                        elif hand1[warStep1] < hand2[warStep]:
                            for i in range (0, len(hand1)):
                                hand2.append(hand1.pop(0))
                            warComplete = True
                            warSum[warSaveSlot] += 1

                        #If the war is still not resolved skip 4 more cards 
                        elif hand1[warStep1] == hand2[warStep]:
                            warStep += 4
                            
#################### If hand2 is shorter than warstep
                        
                    elif warStep2 != 0:
                        if hand2[warStep2] > hand1[warStep]:
                            for i in range (0, warStep +1):
                                hand1.append(hand1.pop(0))
                            warComplete = True
                            warSum[warSaveSlot] += 1
                            
                        elif hand2[warStep2] < hand1[warStep]:
                            for i in range (0, len(hand2)):
                                hand1.append(hand2.pop(0))
                            warComplete = True
                            warSum[warSaveSlot] += 1
                            
                        #If the war is still not resolved skip 4 more cards 
                        elif hand2[warStep2] == hand1[warStep]:
                            warStep += 4

###################################End of War####################################
                                        
            roundNum = roundNum + 1

            #No need to make sure a game doesn't cycle because
            #"On finiteness in the card game war" by Evgeny Lakshtanov,
            #and Vera Roshchina Proved its impossible

 ########This runs when a game has finished                                  
        if len(hand1) != 0:
            playerWins = True
        elif len(hand2) != 0:
            playerWins = False
       
        #Converting the order string into hexadecimal to save memory space
        orderSaved = str(hex(int(order, 2)))

        return hand1Saved, hand2Saved, roundNum, playerWins, orderSaved,
                hand1Sum, hand2Sum, warSum
    
    except:
        print("An Error Occurred, Please Solve")
        print("Player Hand:", hand1Saved)
        print("Computer Hand:", hand2Saved)
        print("Number of Wars:", warSum)
        print("Game order:", order) 

        
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#-------------------------------Core Control Code--------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

while True:
    try:
        mode = input('''For Winner First game enter "W"
                        For Loser First game enter "L"
                        For Random Order game enter "R"
                        To exit enter "C":''')
        
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
############################Higher first###########################

        if mode is 'W':
            for i in range (count):
                hand1Save, hand2Save, rounds, whoWins, hand1Sum, hand2Sum, warSum = WarGameHigherFirst(jokersNum)

                #Reformatting arrays to work with the delimiter
                s = str(hand1Save)
                s1 = s.replace("]","")
                s = str(hand2Save)
                s2 = s.replace("]","")
                s = str(warSum)
                s3 = s.replace("]","")
                s3 = s3.replace(',','[')

                #Saving the data to a text file
                file.write("\n")
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

            file.close()
                
            #Data save order: Game type, Winner Boolean, sum of hand 1,
            #sum of hand 2, number of rounds, starting shuffle of hand 1,
            #starting shuffle of hand 2, number of wars, order of WF/LF)
                
############################Loser first###########################

        elif mode is 'L':
            for i in range (count):
                hand1Save, hand2Save, rounds, whoWins, hand1Sum, hand2Sum, warSum = WarGameLowerFirst(jokersNum)
                
                #Reformatting arrays to work with the delimiter
                s = str(hand1Save)
                s1 = s.replace("]","")
                s = str(hand2Save)
                s2 = s.replace("]","")
                s = str(warSum)
                s3 = s.replace("]","")
                s3 = s3.replace(',','[')

                #Saving the data to a text file
                file.write("\n")
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

            file.close()

            #Data save order: Game type, Winner Boolean, sum of hand 1,
            #sum of hand 2, number of rounds, starting shuffle of hand 1,
            #starting shuffle of hand 2, number of wars, order of WF/LF)
                
############################Random first###########################

        elif mode is 'R':
            for i in range (count):
                hand1Save, hand2Save, rounds, whoWins, orderSaved, hand1Sum, hand2Sum, warSum = WarGameRandomFirst(jokersNum)
                
                #Reformatting arrays to work with the delimiter
                s = str(hand1Save)
                s1 = s.replace("]","")
                s = str(hand2Save)
                s2 = s.replace("]","")
                s = str(warSum)
                s3 = s.replace("]","")
                s3 = s3.replace(',','[')

                #Saving the data to a text file
                file.write("\n")
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

            file.close()

            #Data save order: Game type, Winner Boolean, sum of hand 1,
            #sum of hand 2, number of rounds, starting shuffle of hand 1,
            #starting shuffle of hand 2, number of wars, order of WF/LF)

    ############################To prevent an error############################
        else:
            print('Please enter a valid type of game or enter "C" to cancel')
            
    except:
        print("An error occurred outside of a game")
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
This is still a changing project and will be edited often.

The data from this program will be first saved to a text file.

This data is designed to be then entered into a database with '[' being the
delimiting character.

If any game is saved with a 0 in the rounds column, that means it went to 10,000 rounds and was forced to stop.

There are catches in to keep any errors from causing a fatal crash of the program

The program generally takes 10 minutes to run 1,000,000 games.

There is some optimization that can be done by combining the three functions into
one, but for debugging they were left separate.
''' 

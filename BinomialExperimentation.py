###################################

# Team 18
# 1. Shubham Paul             002011001071(A2)
# 2. Dibyabrata Panja         002011001028(A1)
# 3. Manas Pratim Biswas      002011001025(A1)
# 4. Md Bosirullah Mondal     002011001030(A1)

###################################

# In this assignment, we have performed coin toss experiments which follows 
# the Binomial Distribution.

# At first we have calculated the theoretical probabilites for various number
# of success/Head. We have printed the Binomial Distribution probabilities

# After this we have simulated the coin tosses and calculated the number of occurrences
# for different number of successess/Head as per the experiment multiplier

# Lastly we have physically performed the experiment by tossing coins

# In the above three parts we have theoretically, experimentally and physically 
# compared the various probabilies of getting success by tossing coins which
# follows the Binomial Distribution

###################################

###################################
#  Execution Command : python3 18_2.py [number of trials] [probability of success] [experimental_multiplier]
#  Example Command : python3 18_2.py 3 1/5 4
###################################

###################################

# Sample Input 1 : 3   1/5   4
# Sample Output 1 : 
# -------------------------------------------------------------------------------------------------------
# PART 1 : Calculating probability of success for various number of success
# -------------------------------------------------------------------------------------------------------
# Number of success 		 Probability of success
# X =  0				        P(X = 0)  =  1/8
# X =  1				        P(X = 1)  =  3/8
# X =  2				        P(X = 2)  =  3/8
# X =  3				        P(X = 3)  =  1/8
# -------------------------------------------------------------------------------------------------------
# PART 2 : Simulating coin toss through randomized algorithm
# -------------------------------------------------------------------------------------------------------
# Number of success 		 Number of occurrence
# X =  0				            3
# X =  1				            7
# X =  2				            16
# X =  3				            6
# -------------------------------------------------------------------------------------------------------
# PART 3 : Physically tossing 3 coins simultaneously for 8 times
# -------------------------------------------------------------------------------------------------------
# Number of success 		 Probability of success
# X =  0				        P(X = 0)  =  1/8
# X =  1				        P(X = 1)  =  4/8
# X =  2				        P(X = 2)  =  3/8
# X =  3				        P(X = 3)  =  0/8


# Sample Input 2 : 4   1/4   5
# Sample Output 2 :
# -------------------------------------------------------------------------------------------------------
# PART 1 : Calculating probability of success for various number of success
# -------------------------------------------------------------------------------------------------------
# Number of success 		 Probability of success
# X =  0				        P(X = 0)  =  1/16
# X =  1				        P(X = 1)  =  1/4
# X =  2				        P(X = 2)  =  3/8
# X =  3				        P(X = 3)  =  1/4
# X =  4				        P(X = 4)  =  1/16
# -------------------------------------------------------------------------------------------------------
# PART 2 : Simulating coin toss through randomized algorithm
# -------------------------------------------------------------------------------------------------------
# Number of success 		 Number of occurrence
# X =  0					        1
# X =  1					        27
# X =  2					        32
# X =  3					        19
# X =  4					        1
# -------------------------------------------------------------------------------------------------------
# PART 3 : Physically tossing 3 coins simultaneously for 8 times
# -------------------------------------------------------------------------------------------------------
# Number of success 		 Probability of success
# X =  0				        P(X = 0)  =  1/8
# X =  1				        P(X = 1)  =  4/8
# X =  2				        P(X = 2)  =  3/8
# X =  3				        P(X = 3)  =  0/8
# -------------------------------------------------------------------------------------------------------

###################################

import sys
import random
import math
import fractions
import matplotlib.pyplot as plt
import numpy as np

def toFloat(x):
    arr = x.split('/')
    numerator = float(arr[0])
    denominator = float(arr[1])
    return 1.0*numerator/denominator

def toFraction(x):
    return str(fractions.Fraction(x))

def NCR(n,x):                       #function for calculating nCr
    if(n==x):
        return 1
    if(x==1):
        return n
    if(x==0):
        return 1
    return NCR(n-1,x-1)+NCR(n-1,x)

def binomialProbability(n,x):       #function for calculating Binomial Probability
    probability =  1.0*NCR(n,x)*pow(p,x)*pow(q,n-x)
    return probability

def printingProbabilities():       #function for printing probabilities for all possible number of success
    
    printLine()
    print("PART 1 : Calculating probability of success for various number of success",end="\n")
    printLine()
    
    print("Number of success \t\t Probability of success",end="\n")
    for i in range(0,n+1):
        successValues[i] = int(i)
        probability = binomialProbability(n,i)
        theoreticalProbability[i] = probability
        print("X = ",i, end = "\t\t\t\t")
        print("P(X = %d)"%i," = ",toFraction(probability))
    
    printLine()       


def simulatingCoinToss():           #function for simulating coin toss
    
    print("PART 2 : Simulating coin toss through randomized algorithm",end="\n")
    printLine()
    
    noOfTrials = pow(2,n)
    if(p <= 0.5):
        rangeOfValues = math.floor(1.0/p) - 1
    else:
        rangeOfValues = math.floor(1.0/q) - 1


    if(p <= 0.5):
        for cnt in range (0,experimentalMultiplier):
            for i in range (0,noOfTrials):
                noOfSuccess = 0
                for j in range (0,n):   
                    randomNumber = random.randint(0,rangeOfValues)
                    if(randomNumber==0):
                        noOfSuccess = noOfSuccess+1
                successCount[noOfSuccess] = successCount[noOfSuccess]+1
    else:
        for cnt in range (0,experimentalMultiplier):
            for i in range (0,noOfTrials):
                noOfSuccess = 0
                for j in range (0,n):   
                    randomNumber = random.randint(0,rangeOfValues)
                    if(randomNumber==0):
                        noOfSuccess = noOfSuccess+1
                successCount[n-noOfSuccess] = successCount[n-noOfSuccess]+1

    print("Number of success \t\t Number of occurrence",end="\n")
    for i in range(0,n+1):
        print("X = ",i, end = "\t\t\t\t\t")
        print(successCount[i])
    
    printLine()

def printLine():
    print("-------------------------------------------------------------------------------------------------------",end="\n")

def checkInputs():      #function to check the validity of the inputs
    flag = False
    if(n < 3):
        print("The number of trials should be atleast 3!\n")
        flag = True

    if(p >= 1.0):
        print("The probability of success cannot be greater than equal to 1!\n")
        flag = True

    if(p <= 0.0):
        print("The probability of success cannot be less than equal to 0!\n")
        flag = True

    if(experimentalMultiplier < 1):
        print("Experimental multiplier should be greater than 1!\n")
        flag = True

    if(flag == True):
        exit()

def checkArgs():
    if (argumentLength < 4):
        print("Sufficient number of arguments are not provided!\n")
        quit()

def drawGraphs():
    
    plt.subplot(1,2,1)
    plt.bar(successValues,theoreticalProbability)
    plt.xlabel("Number of success")
    plt.ylabel("Probability")
    plt.title("Probability Distribution")

    plt.subplot(1,2,2)
    plt.bar(successValues,successCount)
    plt.xlabel("Number of success")
    plt.ylabel("Number of occurence")
    plt.title("Occurrence Distribution")

    plt.show()
    

argumentLength = len(sys.argv)
checkArgs()                                         #checking if the arguments are valid

n = (int) (sys.argv[1])                             #number of trials
p = toFloat(sys.argv[2])                            #probability of success of each trial
experimentalMultiplier = (int) (sys.argv[3])        #number of times experiment is performed
q =  1.0-p                                          #probability of failure of each trial


successValues = [0]*(n+1)                           #stores the possible number of success
successCount = [0]*(n+1)                            #stores the number of success 
theoreticalProbability = [0]*(n+1)                  #stores the probability of success

checkInputs()
printingProbabilities()
simulatingCoinToss()
drawGraphs()

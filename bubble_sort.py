# Python program for implementation of Bubble Sort (https://de.wikipedia.org/wiki/Bubblesort#/media/Datei:Bubble-sort-example-300px.gif):
#  - sort an arbitrary array handed as arg list (max size 20)
#  - print unsorted list
#  - print sorted list
#
# Example:
# python bubble_sort.py 1 2 5 12 3
# -> prints
# unsorted: 1 2 5 12 3
# sorted:   1 2 3 5 12 


# Magic Simon was here . __.

#################################################################################


##############################################################
# Forgive me if the code is not an expert python Code.
# I am more confortable in C or C++. :)
# Beginner Python Code to perform a Buble Sorting
##############################################################
# main.py
import sys

#The Bubble Man
def myBubbleSorting(theIputArray): 
    myArrLght = len(theIputArray)
    #Moving through array elements
    for aLoop in range(0, myArrLght -1):
        for bLoop in range (0 , myArrLght-aLoop-1 ):
            #Move in the array from 0 to (myArrLght-aLoop-1)
            #Swap if value at bLoop > value at bLoop+1
            if theIputArray[bLoop] > theIputArray[bLoop+1] :
                #Save the greater value temporarly
                temp = theIputArray[bLoop]
                #Save bLoop+1 at bLoop
                theIputArray[bLoop] = theIputArray[bLoop+1]
                #save now temp value at bLoop +1
                theIputArray[bLoop+1] = temp

if __name__ == "__main__":
    #Store the user Argument
    theIputArray = [int(ArrayElement) for ArrayElement in sys.argv[1:]]

    #Print the Bubble sorted array
    print ( "\n The Input Array Elements are:")
    for myArrLoop in range (len(theIputArray)):
        print("%d" %theIputArray[myArrLoop]),

    # Now let us Bubble Sorted them 
    myBubbleSorting(theIputArray)    
    #Print the Bubble sorted array
    print ( "\nThe Buble Sorted Elements are:")
    for myArrLoop in range (len(theIputArray)):
        print("%d" %theIputArray[myArrLoop]),

        

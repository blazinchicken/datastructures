
from random import randint
import sys
import time

def findPair(arr, type, sum):
    n = len(arr)

    if type == 0:
        return nestedLoops(arr, sum)
    elif type == 1:
        return sortingAlgorithm(arr, sum)
    elif type == 2:
        return hashTable(arr, sum)
    else:
        return None

def nestedLoops(arr, sum): #iterate through near every piece of the array O(n^2)
    n = len(arr)
    
    for l in range(n):
        for j in range(l + 1, n):
            if arr[l] + arr[j] == sum:
                return arr[l], arr[j]
            
    return None

def sortingAlgorithm(arr,sum):
    arr.sort()

    left = 0
    right = len(arr) - 1

    while left < right:
        active_sum = arr[left] + arr[right]

        if active_sum == sum:
            return arr[left], arr[right]
        elif active_sum < sum:
            right -= 1
        else:
            right -= 1
    
    return None
    

def hashTable(arr, sum):
    hash_table = {} # use dict to handle collison

    for num in arr:
        complement = sum - num #what number to search for

        if complement in hash_table:
            return complement, num
        else:
            hash_table[num] = True
    
    return None

def generateRandomNumbers(cnt):
    arr = []

    for i in range(cnt):    
        arr.append(randint(1,cnt))
    
    return arr

def printArray(arr):
    n = len(arr)

    for i in range(0, n):
        print(str(arr[i]) + ' ', end=' ')


    print('\n')

if __name__ == '__main__':
# The parameters from the execution will be used as prameters for the generateRandomNumbers function below.
    if len(sys.argv) != 4: #error handling if more or less than 3 arguments in command line
        print("Use: python3 findPair.py <count> <sum> <algorithm>")
        sys.exit(1)
    if sys.argv[1].isdigit() is False: #error handling if the values arent digits
        exit("Error: None Digit Entered")
    if sys.argv[2].isdigit() is False:
        exit("Error: None Digit Entered")
    if sys.argv[3].isdigit() is False:
        exit("Error: None Digit Entered")
    
# You must receive parameters, i.e., N, K, Algorithm from the command lines like below.
# Python3 SortingArray.py 10000 500 0
    N = int(sys.argv[1]) # how many random numbers
    K = int(sys.argv[2]) # Sum of two numbers looking for
    Algorithm = int(sys.argv[3]) # Your algorithm 0, 1, 2
    if Algorithm not in range(3):
        exit("Error: Out of Bounds Input")

    arr = generateRandomNumbers (N)

    if len(arr) < 100:
        print('Generated numbers')
        printArray(arr)
# Timer Start
    time_start = time.time()
    pair = findPair(arr, Algorithm, K)
    
#Timer end
    time_end = time.time()
    
#Print elapsed time for searching.
    time_elapsed = (time_end - time_start) * 1000 #calculate time in milliseconds
    print("Time Elapsed: ", time_elapsed, "milliseconds")

    if pair:
        print("Pair Found", pair)
    else:
        print("No pair found")


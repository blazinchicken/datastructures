#Name:  Kyron Barrow
#ID: 08865495
#Email: kyronbarrow@unomaha.edu

import math

def bubbleSort(arr):
    n = len(arr)
    temp = 0

    for i in range(n):
        for j in range(0, n-i-1):
            #if out of order: swap
            if arr[j] > arr[j+1]:
                swap(arr, i, j+1)

def selectionSort(arr):
    n = len(arr)

    for i in range(n-1):     #set lowest number to min_idx
        min_idx = i

        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j

    #put min number at front of sorted array
        swap(arr, i, min_idx)


def insertionSort(arr):
    n = len(arr)
    for i in range(1, len(arr)):
        key = arr[i]

        #move elements greater than key to one position ahead of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


def shellSort(arr):
    n = len(arr)
    gap = math.floor(n/2)

    while gap >= 1: 
        for i in range(gap,n):
            j = i
            while(j >= gap and arr[j] < arr[j-gap]):
                swap(arr, j, j-gap)
                j -= gap
        gap = math.floor(gap/2) 

def merge(arr, temp, LEFT, CENTER, RIGHT):
    leftIdx = LEFT
    rightIdx = CENTER+1
    merge_start = LEFT

    while(leftIdx <= CENTER and rightIdx <= RIGHT):
        if arr[leftIdx] <= arr[rightIdx]:
            temp[merge_start] = arr[leftIdx]
            leftIdx += 1
        else: 
            temp[merge_start] = arr[rightIdx]
            rightIdx += 1

        merge_start += 1

    while leftIdx <= CENTER: 
        temp[merge_start] = arr[leftIdx]
        merge_start += 1
        leftIdx += 1

    while rightIdx <= RIGHT:
        temp[merge_start] = arr[rightIdx]
        merge_start += 1
        rightIdx += 1

    for i in range(LEFT, RIGHT+1):
        arr[i] = temp[i]

def mergeSort(arr, temp, left, right):
    if left >= right:
        return
    
    center = math.floor((left + right)/2)
    mergeSort(arr, temp, left, center)
    mergeSort(arr, temp, center+1, right)

    merge(arr, temp, left, center, right)

def quickSort(arr, LEFT, RIGHT):
    if LEFT < RIGHT:
        mid = math.floor((LEFT + RIGHT) / 2)
        pivot = arr[mid]

        leftIdx = LEFT
        rightIdx = RIGHT

        while leftIdx <= rightIdx:
            while arr[leftIdx] < pivot:
                leftIdx += 1
            
            while arr[rightIdx] > pivot:
                rightIdx -= 1
            
            if leftIdx <= rightIdx:
                swap(arr, leftIdx, rightIdx)
                leftIdx += 1
                rightIdx -= 1
        
        quickSort(arr, LEFT, leftIdx-1)
        quickSort(arr, leftIdx, RIGHT)


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def printArray(arr):
    n = len(arr)

    for i in range(0,  n):
        print(str(arr[i]) + ' ', end=' ')

    print('\n')

def generateRandomNumbers(cnt, type):
    # This function will generate Integer array of which size is cnt.
    # The range of the generated numbers is 0 ~ cnt
    # type: 1: totally random numbers, 2: sorted_numbers, 3: reverse-order_numbers, else: not supported
    if type == 1: #type 1

    elif type == 2: #type 2

    elif type == 3: #type 3
    
    else:
        return
    print("This line is only for running skeleton code. Remove this line.")

if __name__ == '__main__':
    # The parameters from the execution will be used as prameters for the generateRandomNumbers function below.
    # You must receive parameters from the command lines like below.
    # > python3 SortingArray.py 3 1000000 6 (create reverse-order numbers (0-1000000 and sort it using QuickSort) 
    arr = generateRandomNumbers( , )

    if len(arr) < 100:
        print('Before sort: ')
        printArray(arr)

    # Timer Start

	# Sorting method will be provided as the second parameter for main args[2]
	# 1: Bubble Sort
	# 2: Selection Sort
	# 3: Insertion Sort
	# 4: Shell Sort
	# 5: Merge Sort
	# 6: Quick Sort
	# Else: Not supported

	#Timer end
	#Print elapsed time for sorting.

	#Print numbers only when the cnt is less than 100
    if len(arr) < 100:
        print('After sort: ')
        printArray(arr)
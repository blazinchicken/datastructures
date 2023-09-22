#Kyron Barrow Linked List 

#Name: Kyron Barrow
#ID:   08865495
#Email:kyronbarrow@unomaha.edu
# You are not allowed to modify this class
class Node:
    def __init__(self, data):
    ## data of the node
        self.data = data
    ## next pointer
        self.next = None
# You can modify this class as you want
class LinkedList:
    def __init__(self):
    ## initializing the head with None
        self.head = None
        self.n = 0
        self.count = 0

    def display(self):
## variable for iteration
        temp_node = self.head
## iterating until we reach the end of the linked list
        while temp_node != None:
## printing the node data
            print(temp_node.data, end='->')
## moving to the next node
            temp_node = temp_node.next
        print('Null')
##############################################
## Implement functions belows
##############################################
# add new node and sort the list
# You can change the return values (from void to any) for each function as you want
# you can add functions as you want
    def sortedAdd(self, value):
        # make new node
        new = Node(value)
        # checks if node is empty clause
        if self.head == None:
            self.head = new
            self.count += 1 
            return
        # still needs to add to the back if data < head data
        # needs to set another variable to the head, then cycle through to the spot where the next value is higher than the current value, then insert into that spot. 
        # to do this you need to set the current.next.next = new.next; current.next = new


        
    def remove(self, idx):
        #check empty case
        if self.head == None:
            return
        
        current = self.head
        #check to see if idx is within the bounds
        if idx > self.count or idx <= 0:
            return
        #remove based on idx-1
            #cycle through the list till the item before the idx that needs to be removed
        for x in range(idx-1):
            current = current.next
        #set the new item to be linked
            #check to see if this is removing the last of the list
        if current.next.next == None:
              current.next = None
              return
        current.next = current.next.next
        
        
# find the maximum values in the list
    def findMax(self):

        current = self.head
        max_value = current.data
        
        if self.count == 1:
            return
        #count through the idx, this can be done by using the self.count 
        for i in range(self.count - 1):
        #compare current.data & current.next.data
            if current.data > current.next.data:
                max_value = current.data
            elif current.data < current.next.data:
                max_value = current.next.data
            
            current = current.next
            
        #set the higher one to be max_value, then try again, counting to self.count-1
        #then return the found value
        
        return max_value in list    
    
# print linkedlist in a reversed order
    def printReversedList(self):
        current = self.head
        listArray = list(self.count) 
        listReversedArray = list(self.count)
        #make an array with self.count (self.count-1) pieces of data, count through the list, making current.data == array[i]
        for i in range(self.count):
            listArray[i] = current.data
        #this creates the list in order, then make another reverse array
        for i in range(self.count):
            listReversedArray[i] = listArray[self.count-1-i]
        #you set arrayTw0[i] = array[self.count-1-i] within a for loop
        for i in range(self.count):
            print(listReversedArray[i])
            print(" ")
        #then in the next for loop print the array

        if __name__ == '__main__':
## instantiating the linked list
            list = LinkedList()


# Your testcase will be here.
# This is a testcase example.
#list.sortedAdd(5)
#list.sortedAdd(2)
#list.sortedAdd(9)
#list.sortedAdd(1)
#list.sortedAdd(7)
#print(list.findMax())
#list.printReversedList()
#################################
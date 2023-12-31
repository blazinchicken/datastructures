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
        while temp_node is not None:
## printing the node data
            print(temp_node.data, end=' -> ')
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
        if value < self.head.data:
            new.next = self.head
            self.head = new
            self.count += 1
            return
        # needs to set another variable to the head, then cycle through to the spot where the next value is higher than the current value, then insert into that spot. 
        current = self.head
        while current.next and value >= current.next.data:
            current = current.next

        new.next = current.next
        current.next = new
        self.count += 1

        # to do this you need to set the new.next = current.next; current.next = new


        
    def remove(self, idx):
        #check empty case
        if self.head == None:
            return
        
        current = self.head
       
        #check to see if idx is within the bounds
        if idx > self.count or idx < 0:
            return
        
        if idx == 0:
            self.head = current.next
            current.next = None
            return

        #remove based on idx-1
            #cycle through the list till the item before the idx that needs to be removed
        for x in range(idx-1):
            current = current.next
        #set the new item to be linked
            #check to see if this is removing the last of the list
        if current.next == None:
              current = None
              return
        current.next = current.next.next
        return
        
        
# find the maximum values in the list
    def findMax(self):

        current = self.head
        max_value = current.data
        if self.head == None:
            return
        if self.count == 1:
            return max_value
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
        
        return max_value     
    
# print linkedlist in a reversed order
#######################################

#needs redesign, start with counting through linked list - 1, then print, then repeat for linked list - 2, -3,..., -n
#this is O(n^2)
#use print with end command as a space, this will allow for no new line
    def printReversedList(self):
        #####################################
        #current = self.head
        #listArray = [] 
        #make empty list, fill with data from list
        #while current is not None:
        #   listArray.append(current.data)
        #    current = current.next
        #this creates the list in order
        #for i in range(len(listArray) - 1, -1, -1):
        #    print(listArray[i])
        #this prints backwards using the reverse count feature of range()
        #then in the next for loop print the array
        #######################################(PREVIOUS ITERATION)
        current = self.head
        reverse = 1
        if self.head == None:  #error handling for empty list
            return
        if self.count == 1:  #error handling for single length list
            print(self.head.data)
            return

        for i in range(self.count): #iterates through the list, this takes a temp value to cycle through to the end of the list then print that value
                                    # it then counts up one and forces the second to last value to be printed
                                    #it does this until no value is left to be printed
            temp = current
            for j in range(self.count - reverse):
                temp = temp.next

            print(temp.data, end=" ")    
            reverse += 1
        print()
        return
       


if __name__ == '__main__':
## instantiating the linked list
    list = LinkedList()


# Your testcase will be here.
# This is a testcase example.
list.sortedAdd(5)
list.sortedAdd(3)
list.sortedAdd(1)
list.sortedAdd(6)
list.sortedAdd(8)
list.sortedAdd(9)
list.display()
print(list.findMax())
list.printReversedList()
list.sortedAdd(2)
list.display()
list.printReversedList()


#print(list.findMax())
#list.printReversedList()
#################################
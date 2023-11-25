class AvlNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.height = 0

class AVLTree:
    def __init__(self):
        self.root = None

    def print_tree(self, key="key", left="left", right="right"):
        def display(root, key=key, left=left, right=right):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if getattr(root, right) is None and getattr(root, left) is None:
                line = '%s' % getattr(root, key)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if getattr(root, right) is None:
                lines, n, p, x = display(getattr(root, left))
                s = '%s' % getattr(root, key)
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if getattr(root, left) is None:
                lines, n, p, x = display(getattr(root, right))
                s = '%s' % getattr(root, key)
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(getattr(root, left))
            right, m, q, y = display(getattr(root, right))
            s = '%s' % getattr(root, key)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        if self.root is None:
            print ("Tree is empty")
            return

        lines, *_ = display(self.root, key, left, right)
        for line in lines:
            print(line)

    ###########################################
    # You need to implement functions from here
    def isEmpty(self):
        if self.root is None:
            return True

        return False

    def insert(self, key): #def from slides, first function
        #Write your code here
        if self.root is None:
            self.root = AvlNode(key)
        else:
            self.root = self._insert(key,self.root)
        #You need to adjust return value
        return None
    
    def _insert(self,key,node):
        if node is None:
            new_node = AvlNode(key)
            return new_node
        
        compareResult = self.compare(key, node.key)

        if compareResult < 0:
            node.left = self._insert(key, node.left)
            
        if (self.height(node.left) - self.height(node.right)) == 2:
            compareResult = self.compare(key, node.left.key)

            if compareResult < 0:
                node = self.rotate_with_left_child(node)
            else:
                node = self.double_rotate_with_left_child(node)
        elif compareResult > 0:
            node.right = self._insert(key, node.right)

            #check balance
            #node added to the right. only -2 is possible for checking
            if (self.height(node.left) - self.height(node.right)) == -2:
                compareResult = self.compare(key, node.right.key)

                if compareResult > 0:
                    node = self.rotate_with_right_child(node)
                else:
                    node = self.double_rotate_with_right_child(node)
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        return node

    def contains (self, key):
        # Write your code here
        # You need to adjust return value
        return None

    # Return the height of node t, or -1, if not found.
    def height(self, key):
        #Write your code here
        #You need to adjust return value
        return -1

    # Return the depth of node t, or -1, if not found.
    def depth(self, key):
        #Write your code here
        #You need to adjust return value
        return -1

    def findMin(self, node=None):
        #Write your code here
        #You need to adjust return value
        return 0

    def findMax(self, node=None):
        #Write your code here
        #You need to adjust return value
        return 0

    # Implemented
    def compare(self, x, y):
        if x < y:
            return -1
        elif x > y:
            return 1
        else:
            return 0

    def rotate_with_left_child(self, k2):
        #LL rotation
        #Write your code here
        #You need to adjust return value
        return None

    def rotate_with_right_child(self, k2):
        #RR rotation
        #Write your code here
        #You need to adjust return value
        return None

    def double_rotate_with_left_child(self, k3):
        # LR rotation
        #Write your code here
        #You need to adjust return value
        return None

    def double_rotate_with_right_child(self, k3):
        # RL rotation
        #Write your code here
        #You need to adjust return value
        return None
    
    def delete(self,key):


        return None
    
def printMenu(): #Print Menu for AVL Tree
    print("========== AVL MENU ==========")
    print(" 0. Show Menu\n 1. Insert A New Key\n 2. Check if Key Exists\n 3. Find The Node's Height\n 4. Find the Node's Depth\n 5. Find the Minimum Value")
    print(" 6. Find the Maximum Value\n 7. Print Tree\n 8. Delete a Key\n 9. Exit")
    return None


if __name__ == '__main__':
    avlTree = AVLTree()
    exitCall = 0

    # Show your menu here and call AvlTree function with parameters
    avlTree.insert(5)
    avlTree.insert(10)
    avlTree.print_tree()

    while exitCall == 0:
        printMenu()

        try:
            choice = int(input("> "))
        except TypeError:
            print("Please enter a valid Number")
        except ValueError:
            print("Please enter a valid Number")
            continue
        
        if choice == 0: #show menu
                printMenu()
        elif choice == 1: #insert new key
            key = print("Input a Key: ")
            print(avlTree.insert(key), "is added to the Tree")
        elif choice == 2: # check if key exists
            key = print("Input a Key: ")
            avlTree.contains(key)
        elif choice == 3: #find height
            key = print("Insert Node: ")
            avlTree.height(key)
        elif choice == 4: #find depth
            key = print("Insert Node: ")
            avlTree.depth(key)
        elif choice == 5: #find minimum value
            avlTree.findMin()
        elif choice == 6: #find max value
            avlTree.findMax()
        elif choice == 7: #print tree
            avlTree.print_tree()
        elif choice == 8: # delete a key
            key = print("Input a Key: ")
            avlTree.delete(key)
        elif choice == 9: #exit
            exitCall = 1
        else:
            print("Invalid Choice, Choose between 1-9")
    
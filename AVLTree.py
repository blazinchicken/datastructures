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
    
    def _insert(self, key, node):
        if node is None:
            return AvlNode(key)

        compareResult = self.compare(key, node.key)

        if compareResult < 0:
            node.left = self._insert(key, node.left)

        # Check balance
            if self.height(node.left) - self.height(node.right) == 2:
                compareResult = self.compare(key, node.left.key)

                if compareResult < 0:
                # LL rotation
                    return self.rotate_with_left_child(node)
                else:
                # LR rotation
                    return self.double_rotate_with_left_child(node)
        elif compareResult > 0:
            node.right = self._insert(key, node.right)

        # Check balance
            if self.height(node.right) - self.height(node.left) == 2:
                compareResult = self.compare(key, node.right.key)

                if compareResult > 0:
                # RR rotation
                    return self.rotate_with_right_child(node)
                else:
                # RL rotation
                    return self.double_rotate_with_right_child(node)

    # Update height after insertion
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        return node



    def contains (self, key):
        # Write your code here
        # You need to adjust return value
        return self._contains(self.root, key)

    def _contains (self, node, key):
        if node is None:
            return False
        
        if key == node.key:
            return True
        elif key < node.key:
            return self._contains(node.left, key)
        else: 
            return self._contains(node.right, key)
        

    # Return the height of node t, or -1, if not found.
    def height(self, node):
        #Write your code here
        if node is None:
            return -1
        #You need to adjust return value
        return node.height
    
    def findNode(self, key):
        return self._findNode(self.root, key)
    
    def _findNode(self, node, key):
        if node is None:
            return None
        
        if key == node.key:
            return node
        elif key < node.key:
            return self._findNode(node.left, key)
        else:
            return self._findNode(node.right, key)

    # Return the depth of node t, or -1, if not found.
    def depth(self, key):
        #Write your code here
        #You need to adjust return value
        return self._depth(self.root, key, 0)

    def _depth(self, node, key, current_depth):
        if node is None:
            return -1
        
        if key == node.key:
            return current_depth
        elif key < node.key:
            return self._depth(node.left, key, current_depth + 1)
        else:
            return self._depth(node.right, key, current_depth + 1)
        
    def findMin(self, node=None):
        #Write your code here
        if self.root is None:
            print("Tree is Empty")
            return None
        #You need to adjust return value
        return self._findMin(self.root).key

    def _findMin(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def findMax(self, node=None):
        #Write your code here
        if self.root is None:
            print("Tree is Empty")
            return None
        #You need to adjust return value
        return self._findMax(self.root).key
    
    def _findMax(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

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
        k1 = k2.left
        k2.left = k1.right
        k1.right = k2
        k2.height = max(self.height(k2.left), self.height(k2.right)) + 1
        k1.height = max(self.height(k1.left), self.height(k2)) + 1
        #You need to adjust return value
        return k1

    def rotate_with_right_child(self, k2):
        #RR rotation
        #Write your code here
        k1 = k2.right
        k2.right = k1.left
        k1.left = k2
        k2.height = max(self.height(k2.left), self.height(k2.right)) + 1
        k1.height = max(self.height(k1.right), self.height(k2)) + 1
        #You need to adjust return value
        return k1

    def double_rotate_with_left_child(self, k3):
        # LR rotation
        #Write your code here
        k3.left = self.rotate_with_right_child(k3.left)
        return self.rotate_with_left_child(k3)
        #You need to adjust return value

    def double_rotate_with_right_child(self, k3):
        # RL rotation
        #Write your code here
        k3.right = self.rotate_with_left_child(k3.right)
        return self.rotate_with_right_child(k3)
        #You need to adjust return value
        
    
    def delete(self, key):
        #Delete 1st function
        if self.root is None:
            print("Tree is Empty")
            return None
        
        success, self.root = self._delete(key, self.root)
        if success:
            print(key, "is deleted from the Tree")
        else:
            print(key, "is not found in the Tree")
    
    def _delete(self, key, node):
        if node is None:
            return False, None
        
        compare_result = self.compare(key, node.key)

        if compare_result < 0:
            deleted, node.left = self._delete(key, node.left)
        elif compare_result > 0:
            deleted, node.right = self._delete(key, node.right)
        else: #found node
            deleted = True
            if node.left is None:
                return deleted, node.right
            elif node.right is None:
                return deleted, node.left
            else: #2 children
                min_node = self.findMin(node.right)
                node.key = min_node.key
                deleted, node.right = self._delete(min_node.key, node.right)
        
        if deleted:
            node.height = 1 + max(self.height(node.left), self.height(node.right))
            balance = self.balance_factor(node)

            #time for rebalance
            if balance > 1:
                if key < node.left.key:
                    return False, self.rotate_with_right_child(node)
                else: 
                    return False, self.double_rotate_with_right_child(node)
            elif balance < -1:
                if key > node.right.key:
                    return False, self.rotate_with_left_child(node)
                else:
                    return False, self.double_rotate_with_left_child(node)
        return deleted, node
    
    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right)
    
def printMenu(): #Print Menu for AVL Tree
    print("========== AVL MENU ==========")
    print(" 0. Show Menu\n 1. Insert A New Key\n 2. Check if Key Exists\n 3. Find The Node's Height\n 4. Find the Node's Depth\n 5. Find the Minimum Value")
    print(" 6. Find the Maximum Value\n 7. Print Tree\n 8. Exit")
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
            key = int(input("Input a Key: "))
            avlTree.insert(key)
            print(key, "is added to the Tree")
        elif choice == 2: # check if key exists
            key = int(input("Input a Key: "))
            result = avlTree.contains(key)
            if result is not None:
                print(result, " is part of the tree")
            else:
                print(key, "is not in the tree")
        elif choice == 3: #find height
            key = int(input("Input a Node: "))
            nodeToFind = avlTree.findNode(key)
            if nodeToFind is not None:
                print(avlTree.height(nodeToFind), "is the height of that Node")
            else:
                print("Node with key", key, "not found in the tree")
        elif choice == 4: #find depth
            key = int(input("Input a Node: "))
            print(avlTree.depth(key), "is the depth of that Node")
        elif choice == 5: #find minimum value
            print(avlTree.findMin(), " is the minimum value in the Tree")
        elif choice == 6: #find max value
            print(avlTree.findMax()," is the max value in the Tree")
        elif choice == 7: #print tree
            avlTree.print_tree()
        elif choice == 8:
            print("Exited Menu") #exit
            exitCall = 1
        else:
            print("Invalid Choice, Choose between 1-9")
    
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

    def insert(self, key):
        #Write your code here
        #You need to adjust return value
        return None

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
while exitCall != 0:
    printMenu()
    input = print("> ")
    if input != range(10):
        print("Menu only supports commands 0-9, please choose another option")
    elif input == 0:
        printMenu()
    elif input == 1:
        key = print("Input a Key: ")
        avlTree.insert(key)
        print(key, "is added to the Tree")
    elif input == 2:
        key = print("Input a Key: ")
        avlTree.contains(key)
    
    
        
    

    # Show your menu here and call AvlTree function with parameters
    avlTree.insert(5)
    avlTree.insert(10)
    avlTree.print_tree()
#Name: Kyron Barrow
#ID: 08865495   
#Email: kyronbarrow@unomaha.edu

class Calculator:
    def __init__(self):
        self.stack = []

    def convert(self, infix):
        # use a stack to covert infix to postfix
        self.stack.clear()
        postfix = "postfix from infix"# output
        
        # You are not allowed to add additional functions e.g., precedence(), isOperator(), etc.
        # You are not allowed to create variables using a list or a dictionary like below. 
        #    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        #    operators = ['(', ')', '-', '+', '*', '/', '^']
        # Keep the pseudo code (for loops) below with your code.
        #==================================================================================================
        #for c in infix:
        #    if c == '(' stack.push(c):
        if c == '(':
            self.stack.push(c)
            
        #    else if c == ')':
        #        while stack.isEmpty() == false && stack.peek() != '(':
        #            poped_char = stack.pop() and postfix.append(poped_char)
        #    else if c == '+' || c == '-':
        #        while stack.isEmpty() == false && stack.peek() == ‘/’ || ‘*’ || ‘+’ || ‘-’
        #            poped_char = stack.pop() and postfix.append(poped_char)
        #    else if c == ‘/’ || c == ‘*’
        #        while stack.isEmpty() == false && stack.peek() == ‘/’ || ‘*’
        #            poped_char = stack.pop() and postfix.append(poped_char)
        #    else:
        #        stack.push(c)

        #while stack.isEmpty() == false:
        #    poped_char = stack.pop() and postfix.append(poped_char)

        #return postfix
        #==================================================================================================
    # This Return double for division
    def evaluate(self, postfix):
        #Use stack of tokens
        self.stack.clear()
        
        # Keep the instructions below with your code.
        # implement as directed
        #• Repeat
        #• If operand, push onto stack
        #• If operator
        #   • pop operands off the stack
        #   • evaluate operator on operands
        #   • push result onto stack
        #• Until expression is read
        #• Return top of stack

        result = 0
        return result


if __name__ == '__main__':
    ## instantiating the linked list
    cal = Calculator()

    #input = ; # Get input from a user

    postfix = cal.convert(input)
    print(postfix)

    result = cal.evaluate(postfix)
    print(result)



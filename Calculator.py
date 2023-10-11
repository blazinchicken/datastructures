#Name: Kyron Barrow
#ID: 08865495   
#Email: kyronbarrow@unomaha.edu

class Calculator:
    def __init__(self):
        self.stack = []

    def convert(self, infix):
        # use a stack to covert infix to postfix
        self.stack.clear()
        postfix = []# output
        
        # You are not allowed to add additional functions e.g., precedence(), isOperator(), etc.
        # You are not allowed to create variables using a list or a dictionary like below. 
        #    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        #    operators = ['(', ')', '-', '+', '*', '/', '^']
        # Keep the pseudo code (for loops) below with your code.
        #elif c == '/' or '*':
        #       while self.stack and (self.stack[-1] == "*" or self.stack[-1] == '/'):
        #            poped_char = self.stack.pop()
        #            postfix.append(poped_char)
        #        self.stack.append(c)
        #==================================================================================================
        #for c in infix:
        for c in infix:
            if c.isdigit():
                postfix.append(c)
        #    else if c == '+' || c == '-':
            elif c in ['+','-']:
                while self.stack and (self.stack[-1] in ['+','-','*','/']): #        while stack.isEmpty() == false && stack.peek() == ‘/’ || ‘*’ || ‘+’ || ‘-’
                    poped_char = self.stack.pop()   #poped_char = stack.pop() and postfix.append(poped_char)
                    postfix.append(poped_char)
                self.stack.append(c)
            elif c in ['/','*']: #    else if c == ‘/’ || c == ‘*’
                    while self.stack and (self.stack[-1] in ['/','*']): #     while stack.isEmpty() == false && stack.peek() == ‘/’ || ‘*’
                        poped_char = self.stack.pop()    #         poped_char = stack.pop() and postfix.append(poped_char)
                        postfix.append(poped_char)
                    self.stack.append(c)
            #elif c == '(' stack.push(c):
            elif c == '(':              
                self.stack.append(c)
        #    else if c == ')':
            elif c == ')':
        #        while stack.isEmpty() == false && stack.peek() != '(':
                while self.stack and self.stack[-1] != '(':
        #            poped_char = stack.pop() and postfix.append(poped_char)
                    poped_char = self.stack.pop()
                    postfix.append(poped_char)
                self.stack.pop()
     
        #while stack.isEmpty() == false:
        while self.stack:

        #    poped_char = stack.pop() and postfix.append(poped_char)
            poped_char = self.stack.pop()
            postfix.append(poped_char)

        #return postfix
        return postfix
        #==================================================================================================
    # This Return double for division
    def evaluate(self, postfix):
        #Use stack of tokens
        self.stack.clear()
        
        # Keep the instructions below with your code.
        # implement as directed
        for c in postfix: #• Repeat
            if c.isdigit():
                self.stack.append(float(c))
            elif c in ['+', '-', '*', '/', '^']: #• If operator
                if len(self.stack) < 2:
                    return
                operand2 = self.stack.pop() #   • pop operands off the stack
                operand1 = self.stack.pop()
                if c == '+':    #   • evaluate operator on operands
                    self.stack.append(operand1 + operand2)  #   • push result onto stack
                elif c == '-':  #   • evaluate operator on operands
                    self.stack.append(operand1 - operand2)   #   • push result onto stack
                elif c == '*':  #   • evaluate operator on operands
                    self.stack.append(operand1 * operand2)   #   • push result onto stack
                elif c == '/':  #   • evaluate operator on operands
                    if operand2 == 0:
                        return
                    self.stack.append(operand1 / operand2)   #   • push result onto stack
                elif c == '^':  #   • evaluate operator on operands
                    if operand2 == 0:
                        self.stack.append(1)
                    else:
                        self.stack.append(operand1 ** operand2)  #   • push result onto stack
                else:   #• Until expression is read
                    return
                
        if len(self.stack) == 1:
            return self.stack[0] #• Return top of stack
        else:
            return

if __name__ == '__main__':
    ## instantiating the linked list
    cal = Calculator()

    input = input("Enter Equation: ") # Get input from a user

    postfix = cal.convert(input)
    print(postfix)

    result = cal.evaluate(postfix)
    print(result)



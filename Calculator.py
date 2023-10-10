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
        for c in infix:

        #    if c == '(' stack.push(c):
            if c == '(':              
                self.stack.push(c)

        #    else if c == ')':
            elif c == ')':

        #        while stack.isEmpty() == false && stack.peek() != '(':
                while self.stack.isEmpty() == False and self.stack.peek() != '(':
                    
        #            poped_char = stack.pop() and postfix.append(poped_char)
                    poped_char = self.stack.pop()
                    postfix.append(poped_char)

        #    else if c == '+' || c == '-':
            elif c == '+' or c == '-':

        #        while stack.isEmpty() == false && stack.peek() == ‘/’ || ‘*’ || ‘+’ || ‘-’
                while self.stack.isEmpty() == False and self.stack.peek() == '/' or '*' or '+' or '-':

        #            poped_char = stack.pop() and postfix.append(poped_char)
                    poped_char = self.stack.pop() and postfix.append(poped_char)

        #    else if c == ‘/’ || c == ‘*’
            elif c == '/' or c == '*':

        #        while stack.isEmpty() == false && stack.peek() == ‘/’ || ‘*’
                while self.stack.isEmpty() == False and self.stack.peek() == '/' or '*':

        #            poped_char = stack.pop() and postfix.append(poped_char)
                    poped_char = self.stack.pop()
                    postfix.append(poped_char)

        #    else:
            else:

        #        stack.push(c)
                self.stack.push(c)

        #while stack.isEmpty() == false:
        while self.stack.isEmpty() == False:

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
            if c in range(10):
                self.stack.append(float(char)) #• If operand, push onto stack
            elif c is '+' or '-' or '*' or '/' or '^': #• If operator
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
                else:   
                    return
                

        
        
       
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



"""StackandQueue"""

class ArrayStack:
    """S"""

    def __init__(self):
        """Generate list"""
        self.data = []

    def size(self):
        """Return Size of Stack"""
        sizes = len(self.data)
        return sizes

    def is_empty(self):
        """Return true if stack empty if not empty return false"""
        if len(self.data) == 0:
            return True
        else:
            return False

    def push(self, data):
        """Push data in stack or last of list"""
        info = self.data
        info.append(data)
        return self

    def pop(self):
        """Pop data in top of stack or last of list"""
        if len(self.data) == 0:
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            arr = list(self.data)[-1]
            self.data.pop()
            return arr

    def stackTop(self):
        """Show data on top of stack or first in list"""
        if len(self.data) == 0:
            print("Underflow: Cannot get StackTop data from an empty list")
            return None
        else:
            return (list(self.data))[-1]

    def printStack(self):
        """Print stack or list"""
        # print(self.data)
        print("--------Newstack--------")
        print()
        for i in range(len(self.data)-1, -1, -1):
            if i == 0:
                print("        "+"|   %s   |" %self.data[i])
                print("        "+"__________")
            else:
                print("        "+"|   %s   |" %self.data[i])
        print()

# myStack = ArrayStack()
# myStack.push(10)
# myStack.push(20)
# myStack.push(30)
# print(myStack.size())
# myStack.printStack()
# x = myStack.pop()
# myStack.printStack()
# myStack.pop()
# myStack.printStack()
# myStack.pop()
# myStack.printStack()
# print(myStack.is_empty())
# myStack.pop()

####################################################################################################

# expression = "(((A+B)*C))"

# def is_parentheses_matching(expression):
#     """Lab4.1"""
#     tempStack = ArrayStack()
#     for i in expression:
#         if i == "(":
#             tempStack.push("(")
#         elif i == ")" and (tempStack.is_empty() or tempStack.stackTop() == ")"):
#             tempStack.push(")")
#         elif i == ")":
#             tempStack.pop()
#         else:
#             pass
#         tempStack.printStack()
#     if tempStack.is_empty() is True:
#         print("Parentheses in %s are matched" %expression)
#         return True
#     else:
#         print("Parentheses in %s are unmatched" %expression)
#         return False

# print(is_parentheses_matching(expression))

####################################################################################################

# def copyStack(stack1, stack2):
#     """Copy Stack"""
#     while not stack2.is_empty():
#         stack2.pop()
#     stack3 = ArrayStack()
#     while not stack1.is_empty():
#         fordup = stack1.pop()
#         stack3.push(fordup)
#     while not stack3.is_empty():
#         fordup1 = stack3.pop()
#         stack1.push(fordup1)
#         stack2.push(fordup1)
#     return


# s1 = ArrayStack()
# s1.push(10)
# s1.push(20)
# s1.push(30)
# s2 = ArrayStack()
# s2.push(15)
# copyStack(s1, s2)
# s1.printStack()
# s2.printStack()

####################################################################################################

# def infixToPostfix(expression):
#     """Infix ---> Postfix"""
#     symStack = ArrayStack()
#     new_mes = ""
#     for i in str(expression):
#         if i == "*":
#             if symStack.is_empty() is True:
#                 symStack.push(i)
#             else:
#                 while ((symStack.is_empty() is False) and\
#                      ((symStack.stackTop() == "/") or (symStack.stackTop() == "*"))):
#                     if symStack.is_empty():
#                         break
#                     else:
#                         sym = symStack.pop()
#                         new_mes += sym
#                 symStack.push(i)
#         elif i == "/":
#             if symStack.is_empty() is True:
#                 symStack.push(i)
#             else:
#                 while ((symStack.is_empty() is False) and\
#                      ((symStack.stackTop() == "*") or (symStack.stackTop() == "/"))):
#                     if symStack.is_empty():
#                         break
#                     else:
#                         sym = symStack.pop()
#                         new_mes += sym
#                 symStack.push(i)
#         elif i == "+":
#             if symStack.is_empty() is True:
#                 symStack.push(i)
#             else:
#                 while ((symStack.is_empty() is False) and\
#                      ((symStack.stackTop() == "*") or (symStack.stackTop() == "/") or\
#                          (symStack.stackTop() == "-") or (symStack.stackTop() == "+"))):
#                     if symStack.is_empty():
#                         break
#                     else:
#                         sym = symStack.pop()
#                         new_mes += sym
#                 symStack.push(i)
#         elif i == "-":
#             if symStack.is_empty() is True:
#                 symStack.push(i)
#             else:
#                 while ((symStack.is_empty() is False) and\
#                      ((symStack.stackTop() == "*") or (symStack.stackTop() == "/") or\
#                          (symStack.stackTop() == "+") or (symStack.stackTop() == "-"))):
#                     if symStack.is_empty():
#                         break
#                     else:
#                         sym = symStack.pop()
#                         new_mes += sym
#                 symStack.push(i)
#         else:
#             new_mes += i
#         print(new_mes)
#         symStack.printStack()
#     while symStack.is_empty() is False:
#         if symStack.is_empty():
#             break
#         else:
#             sym = symStack.pop()
#             new_mes += sym
#     print(new_mes)
#     symStack.printStack()
#     return new_mes

# exp = "A+B+C+D"
# # exp = "A+C+E-D/B"
# # exp = "A+B*C-D/E"
# # exp = "A*B+C-D*F-E"
# # exp = "A+B*C+D"
# postfix = infixToPostfix(exp)
# print("Postfix of '" + exp + "' is '" + postfix + "'")

####################################################################################################

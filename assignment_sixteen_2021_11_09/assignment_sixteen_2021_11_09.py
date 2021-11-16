# 1. Complete and test the (singly)linked and array implementations of stack 
# data structure. as discussed in class. Just like in assignment 15, combine
# stack interface, abstract stack and abstract collection classes into one 
# AbstractStack class (that is this class needs to have ABC class as parent). 

# 2. Your textbook writes about using stack to convert expression from infix into 
# postfix form. Write Python program that will convert infix expression into prefix 
# (Polish) form. You should use the algorithm presented on this website
# https://www.javatpoint.com/convert-infix-to-prefix-notation

# infix:    a + b
# postfix:  a b +
# prefix:   + a b
# infix:    (a + b) * c
# postfix:  a b + c *
# prefix:   * c + a b
# infix:    a + b * c
# postfix:  a b c * +
# prefix:   + * b c a

# Assume infix is correct.
# use math symbols as per the link: (+-*/^)

from node_stack import NodeStack

def main():
    data = input("Enter infix equation: ")
    
    print()
    
    print("Prefix Format: ")
    print(convert_infix(data))

ops = {'+': 0, '-': 0, '/': 1, '*': 1, '^': 2}

def convert_infix(infix: str) -> str:
    revIter = reversed(infix)
    exp = ""
    stack = NodeStack()
    
    for c in revIter:
        if c == ' ': continue
        if c == ')':
            stack.push(c)
            continue
        elif c == '(':
            pop = stack.pop()
            while pop != ')':
                exp += pop
                pop = stack.pop()
            continue
        
        weight = ops.get(c, None)
        if weight != None:
            # operators!
            try:
                p = stack.peek()
                if p == ')':
                    stack.push(c)
                elif weight >= ops.get(p):
                    stack.push(c)
                else:
                    while weight < ops.get(p):
                        exp += stack.pop()
                        p = stack.peek()
                        
                        if p == ')':
                            break
                    stack.push(c)
            except KeyError:
                # no data to peek!
                stack.push(c)
        else:
            # operands!
            exp += c
    
    for x in range(stack.size):
        exp += stack.pop()
    
    # reverse and return the output
    
    # debug
    # print(exp)
    
    outputIter = reversed(exp)
    output = ""
    for x in outputIter:
        output += x
    return output

if __name__ == "__main__":
    main()
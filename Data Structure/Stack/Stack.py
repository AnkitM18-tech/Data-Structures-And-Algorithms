#Funtion Calling is managed by using a stack
#Undo functionality in any editor uses stack to track down last set of operations.
#Push/Pop---->O(1)
#Search element by value---->O(n)
#LIFO(Last In First Out Structure)

"""from collections import deque
stack=deque()
stack.append("-------")
stack.pop()   #Remove Last element"""

from collections import deque


class Stack:
    def __init__(self):
        self.container=deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def isEmpty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

"""def reverse_string(s):
    stack=Stack()

    for char in s:
        stack.push(char)

    rstr=""

    while stack.size()!=0:
        rstr+= stack.pop()

    return rstr

if __name__=="__main__":
    print(reverse_string("We will win against COVID"))"""    #reverse string using stack

"""def is_matched(ch1,ch2):
    match_dict={")":"(","}":"{","]":"["}
    return match_dict[ch1]==ch2

def is_balanced(s):
    stack=Stack()
    for ch in s:
        if ch=="(" or ch=="[" or ch=="{":
            stack.push(ch)
        if ch==")" or ch=="]" or ch=="}":
            if stack.size()==0:
                return False
            if not is_matched(ch,stack.pop()):
                return False
    return stack.size()==0


if __name__ == '__main__':                                       #bracket matching using stack
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))"""
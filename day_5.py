
# Day 5

# 1. Warm-up — Implement a Stack

class Stack:
    
    def __init__(self):
        self.top = -1
        self.arr = []
    
    def push(self,e):
        self.top += 1
        self.arr.append(e)
    
    def pop(self):
        val = self.arr[self.top]
        self.arr.pop()
        self.top -= 1
        return val
    
    def peek(self):
        return self.arr[self.top]
    

s = Stack()
s.push(1)
s.push(2)
print(s.peek())  # 2
print(s.pop())   # 2
print(s.peek())  # 1

"""
Problem 2: Valid Parentheses — think about it like a physical action, not code yet

Take "{[]}" and literally act it out with your hands, one character at a time:

See { → it's an opening bracket. You don't know yet if it'll be closed correctly, so you just... set it aside, remembering it's open. Push it.
See [ → another opener. Set it aside too, on top of the {. Push it.
See ] → a closer. Ask yourself: "does this match the most recently opened bracket I haven't closed yet?" The most recent one you set aside was [. Does ] match [? Yes. Pop it off — that pair is resolved.
See } → another closer. What's the most recent unresolved opener now? {. Does } match {? Yes. Pop it.
String's done. Anything left unresolved (still in the stack)? No — stack is empty. Valid.
"""
    
def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}  # closer -> matching opener
    
    for char in s:
        if char in '([{':
            # it's an opener — what do you do with it?
            stack.append(char)
        else:
            pass
            # it's a closer — what two things do you need to check?
            # 1. is the stack even non-empty? (nothing to match against)
            # 2. does stack's top match pairs[char]?
            if(len(stack)==0): return False
            
            if(stack[-1] == pairs[char]):
                stack.pop()
            else:
                return False
            
            
            
    
    # after the loop: what does "fully valid" mean about the stack's state?
    return len(stack) == 0
    
print(is_valid("()[]{}"))
    

"""
Problem 3: Min Stack — build the idea first, forget code

The hard part: get_min() must be O(1) — no scanning. So the minimum has to be known ahead of time, tracked as you go, not searched for.

Idea: keep a second stack, min_stack, that mirrors every push/pop of the main stack — but at each position, it stores "what was the smallest value so far, up to and including this push."

Trace push(3), push(5), push(2):

action	main stack	min_stack	why
push(3)	[3]	[3]	first element, it's the min so far
push(5)	[3,5]	[3,3]	5 isn't smaller than current min (3), so min_stack repeats 3
push(2)	[3,5,2]	[3,3,2]	2 is smaller than 3, so new min is 2
"""
class MinStack:
    
    def __init__(self):
        self.top = -1
        self.arr = []
        self.min = []
    
    def push(self,e):
        self.top += 1
        self.arr.append(e)
        if(len(self.min) == 0):
            return self.min.append(e)
            
        if (self.min[-1] < e):
            self.min.append(self.min[-1])
        else:
            self.min.append(e)
        # print(self.min)
    
    def pop(self):
        val = self.arr[self.top]
        self.arr.pop()
        self.top -= 1
        self.min.pop()
        return val
    
    def peek(self):
        return self.arr[self.top]
        
    def get_min(self):
        return self.min[-1]
    

s = MinStack()
s.push(3)
s.push(5)
s.push(2)
print(s.get_min())  # 2
s.pop()
print(s.get_min())  # 3  

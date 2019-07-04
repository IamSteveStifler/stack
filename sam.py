"""
Code for implementation of Stack with the help of Python 3.6
"""
class Stack():
    
    def __init__(self):
        self.items = []
     
    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        return self.items.pop()
    
    def is_Empty(self):
        return self.items == []
    
    def top(self):
        if not self.is_Empty():
            return self.items[-1]
    
    def print_stack(self):
        return self.items

s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.push("D")
s.pop()
print(s.top())
print(s.print_stack())

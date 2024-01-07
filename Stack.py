class Stack:
    def __init__(self,*a) -> None:
        self.stack = list(a)
    def push(self,a) -> None :
        self.stack.append(a)
    
    def pop(self,a) -> None :
        self.stack.pop(a)

class Stack:
    def __init__(self, x = []):
        self.x = []
        for i in x:
            self.push(i)

    def isEmpty(self):
        temp = self.x
        if len(temp) == 0:
            print("Obviously, the stack is empty.")
        else:
            length = len(temp)
            print("Obviously, the stack is not empty")
            print("The length of the stack is {}".format(length))

    def push(self, new):
        return self.x.append(new)

    def pop(self):
        temp = self.x
        if len(temp) == 0:
           print("The stack is empty, you can't do that")
        else:
            return self.x.pop()

    def top(self):
        temp = self.x
        if len(temp) == 0:
           print("The stack is empty, you can't do that")
        else:
            temp = self.x[-1]
            print("The top of the stack is {}.".format(temp))

    def bottom(self):
        temp = self.x
        if len(temp) == 0:
           print("The stack is empty, you can't do that")
        else:
            temp = self.x[0]
            print("The bottom of the stack is {}.".format(temp))

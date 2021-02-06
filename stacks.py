class Stack():
    def __init__(self):
        self.items = []
    def pop(self):
        return self.items.pop()
    def push(self, item):
        self.items.append(item)
    def peek(self):
        if len(self.items) != 0:
            return self.items[len(self.items)-1]
    def is_empty(self):
        return len(self.items) == 0
    def get_stack(self):
        return self.items

#Convert an integer into binary
def div_by_2(dec_num):
    s = Stack()
    while dec_num > 0:
        rem = dec_num % 2
        s.push(rem)
        dec_num = dec_num //2
    bin_num = ""
    bin_num += str(s.pop())
    return bin_num

print(div_by_2(121))

#Reverse a string
def rev_string(stack, string):
    # s = Stack()
    rev_string = ""
    for char in string:
        stack.push(char)
    while not stack.is_empty():
        rev_string += stack.pop()
    return rev_string


s = Stack()
print(rev_string(s, 'Hello'))
#olleH
#str[::-1]

#Sort stack such that the smallest items are on the top
class Stack():
    def __init__(self):
        self.items = []
        self.temp = []
    def push(self, item):
        if len(self.items) > 0:
            while self.items and item > self.items[-1]:
                x = self.items.pop()
                self.temp.append(x)
            self.items.append(item)
            while len(self.temp) != 0:
                x = self.temp.pop()
                self.items.append(x)
        else:
            self.items.append(item)
                    
    def pop(self):
        self.items.pop()
    def peek(self):
        return self.items[-1]
    def isEmpty(self):
        return len(self.items) == 0
    def print(self):
        print(self.items)
    
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
s.push(4)
s.print()

#Implement a queue using 2 stacks
class Queue():
    def __init__(self):
        self.items = []
        self.temp = []
    def enqueue(self, item):
        if len(self.items) == 0:
            self.items.append(item)
        else:
            while len(self.items) != 0:
                x = self.items.pop()
                self.temp.append(x)
            self.items.append(item)
            while len(self.temp) != 0:
                x = self.temp.pop()
                self.items.append(x)
    def dequeue(self):
        self.items.pop()
    def print(self):
        print(self.items)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.print()

#Stack with function min which returns the min element in O(n)
class Stack():
    def __init__(self):
        self.items = []
    def push(self, num):
        if len(self.items) == 0:
            self.items.append([num, num])
        else:
            min_ = self.get_min()
            if num < min_:
                min_ = num
            self.items.append([num, min_])
    def pop(self):
        self.items.pop()
    def get_min(self):
        return self.items[-1][1]

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(-1)
print(s.get_min())


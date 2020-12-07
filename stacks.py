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



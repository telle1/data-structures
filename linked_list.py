class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LList():
    def __init__(self):
        self.head = None

    def print_llist(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return self.head

        # while self.head.next:
        #     self.head = self.head.next
        # self.head.next = new_node

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, data, prev_node):
        if not prev_node: #if prev_node is None:
            print ("previous node not in list")
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    #no duplicates
    def delete(self, data):
        #need to consider if its a head or not the head
        #make sure the list is not empty
        cur_node = self.head
        if cur_node and data == cur_node.data:
            self.head = cur_node.next #change head to point to the next node in the list
            cur_node = None #this will get rid of the prior element
            return
        #delete a node that is not the head node
        prev = None
        while cur_node and cur_node.data != data:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None: #the data element is not in the list
            return
        #else
        prev.next = cur_node.next
        cur_node = None

    def delete_at_i(self, i):
        #when position is 0
        #any other number than the head
        cur_node = self.head
        if i == 0:
            self.head = cur_node.next
            cur_node = None
            return
        # else:
        prev = None
        count = 0
        while cur_node and count != i:
            prev = cur_node
            cur_node = cur_node.next
            count +=1
        if cur_node is None: #the position was greater than the number of elements
            return 
        prev.next = cur_node.next
        cur_node = None

    def length(self):
        count = 0
        if self.head is None:
            return 0
        cur_node = self.head
        while cur_node:
            cur_node = cur_node.next
            count += 1
        return count

    def length_recursive(self, node): #<- node is the start of the list
        if node is None:
            return 0
        return 1 + self.length_recursive(node.next)

    def swap_nodes(self, key_1, key_2):
        #case 1:node1 and 2 are not head nodes
        #case 2: node1 and 2 are head nodes
        if key_1 == key_2:
            return
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2
        if not curr_1 or not curr_2:
            return 


llist_ex = LList()

llist_ex.append('B')
llist_ex.append('C')
llist_ex.append('D')
llist_ex.append('E')
llist_ex.append('G')
llist_ex.prepend('A')
llist_ex.delete('A')
llist_ex.insert('F', llist_ex.head.next)
llist_ex.delete_at_i(1)
llist_ex.print_llist()
print(llist_ex.length())
print(llist_ex.length_recursive(llist_ex.head))


llist_2 = LList()
print(llist_2.length())

from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current <= (self.capacity - 1):  # setup
            self.storage.add_to_tail(item)
            self.current += 1
        else:
            idx = self.current % self.capacity

            head_to_update = self.storage.head

            for i in range(idx):
                head_to_update = head_to_update.next

            head_to_update.value = item

            self.current += 1

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        current_node = self.storage.head

        while current_node is not None:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next

        return list_buffer_contents
# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.current] = item
        if self.current < (self.capacity - 1):
            self.current += 1
        else:
            self.current = 0

    def get(self):
        return [i for i in self.storage if i != None]

 # rbf = ArrayRingBuffer(3)
    # rbf.append(1)
    # rbf.append(2)
    # rbf.append(3)
    # rbf.append(4)
    # rbf.append(5)
    # rbf.append(6)
    # rbf.append(7)
    # print(rbf.get())

    bf = RingBuffer(3)
    bf.append(1)
    bf.append(2)
    bf.append(3)
    print(bf.get())

    bf.append(4)
    print(bf.get())

    bf.append(5)
    print(bf.get())

    bf.append(6)
    print(bf.get())

    bf.append(7)
    print(bf.get())

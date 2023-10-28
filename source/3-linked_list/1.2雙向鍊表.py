class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


if __name__ == "__main__":
   head = Node(data = 0)

   node1 = Node(data = 1)
   head.next = node1
   node1.prev = head

   node2 = Node(data = 2)
   node1.next = node2
   node2.prev = node1

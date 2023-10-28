class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

if __name__ == "__main__":
   head = Node(data = 1)
   node1 = Node(data = 2)
   node2 = Node(data = 3)
   head.next = node1
   node1.next = node2

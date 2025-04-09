# realization -> https://www.youtube.com/watch?v=ZND9upTY1hU

class Node:
    def __init__(self, val: int, next=None) -> None:
        self.val = val 
        self.next = next 

class LinkedList:
    def __init__(self, root) -> None: 
        self.root = root 
    
    def append(self, val:int) -> None:
        tmp = self.root
        while tmp.next:
            tmp = tmp.next 
        tmp.next = Node(val=val)

    def output(self) -> None: 
        tmp = self.root 
        while tmp: 
            print(tmp.val, end = " ")
            tmp = tmp.next 
        print("")

    def search(self, val: int) -> bool:
        tmp = self.root 
        while tmp:
            if tmp.val == val:
                return True 
            tmp = tmp.next
        return False 
    
    def pop(self, val: int = None):
        tmp = self.root 
        if tmp.next.next:
            while tmp.next.next:
                if tmp.val == val:
                    return True 
                tmp = tmp.next 
            tmp.next = None  

    def reverse(self):
        prev = None 
        current = self.root 
        while current:
            nxt = current.next 
            current.next = prev 
            prev = current 
            current = nxt
        self.root = prev

    
root = Node(10)
ll = LinkedList(root=root)
ll.append(15)
ll.append(30)
ll.output()
print(ll.search(15))

ll.pop()
ll.output()
ll.reverse()
ll.output()
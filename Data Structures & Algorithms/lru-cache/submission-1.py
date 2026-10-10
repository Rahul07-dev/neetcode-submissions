class Node:
        def __init__(self,key=0,value=0):
            self.key ,self.value=key,value
            self.prev=None
            self.next=None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache ={}
        self.head, self.tail= Node(), Node() 
        self.head.next=self.tail
        self.tail.prev=self.head
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1;
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node= Node(key,value)
        self.cache[key]=node
        self.insert(node)
        if len(self.cache) > self.cap:
           lru=self.head.next
           self.remove(lru)
           del self.cache[lru.key]
    
    def insert(self,node):
        prv, nxt = self.tail.prev , self.tail
        prv.next=node
        nxt.prev=node
        node.prev=prv
        node.next= nxt

    def remove(self,node :Node) -> bool:
        prv,nxt= node.prev,node.next
        prv.next, nxt.prev= nxt,prv        
    

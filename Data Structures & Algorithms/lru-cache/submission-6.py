class Node:
    def __init__(self, key: int = 0, val: int = 0, prev: Node=None, next: Node=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):

        # store dictionary as {key : pointer}
        self.dic = {}
        self.capacity = capacity
        self.currSize = 0
        
        # double linked list to represent the order of used
        self.recent = Node() # tail: most recently used, append
        self.oldest = Node() # head: most recently unused, remove
        # use dummy nodes
        self.oldest.next = self.recent
        self.recent.prev = self.oldest

    def _removeNode(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _addNewNode(self, node: Node) -> None:
        # insert it before dummy recent node
        before = self.recent.prev

        # node before dummy
        before.next = node
        node.prev = before
        # dummy node
        node.next = self.recent
        self.recent.prev = node

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            # update recently used
            self._removeNode(node)
            self._addNewNode(node)

            return self.dic[key].val
        return -1

    def put(self, key: int, value: int) -> None:

        
        if key in self.dic:
            node = self.dic[key]
            # update linked list for recents
            node.val = value # update value
            self._removeNode(node)
            self._addNewNode(node)
        
        else:
            newNode = Node(key, value)
            # if it's already at it's limit, remove oldest before adding
            if self.currSize >= self.capacity:
                # rembmer it's a dummy, so it's the next one
                lru = self.oldest.next
                self._removeNode(lru) 
                del self.dic[lru.key]
                self.currSize -= 1
            
            # now there's room, just add
            self._addNewNode(newNode)
            self.dic[key] = newNode
            self.currSize += 1

        

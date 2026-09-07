class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # HashMap: key -> corresponding node
        self.cache = {}

        # Dummy head and tail nodes
        # head.next -> Least Recently Used (LRU)
        # tail.prev -> Most Recently Used (MRU)
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head


    def remove(self, node):
        # Remove the node from its current position
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev


    def insert(self, node):
        # Insert the node before tail as the Most Recently Used (MRU)
        prev = self.tail.prev   
        tail = self.tail

        prev.next = node
        tail.prev = node

        node.prev = prev
        node.next = tail


    def get(self, key: int) -> int:
        # Return -1 if the key does not exist
        if key not in self.cache:
            return -1

        # Get the node and move it to the MRU position
        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.value


    def put(self, key: int, value: int) -> None:
        # Remove the existing node if the key already exists
        if key in self.cache:
            existing_node = self.cache[key]
            self.remove(existing_node)

        # Create and insert the new node as MRU
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)

        # Remove the LRU node if capacity is exceeded
        if len(self.cache) > self.capacity:
            lru_node = self.head.next

            self.remove(lru_node)
            del self.cache[lru_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)

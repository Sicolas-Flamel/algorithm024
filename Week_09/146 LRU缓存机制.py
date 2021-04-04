class LRUCache(object):
    
    def __init__(self, capacity):
        self.dic = collections.OrderedDict()
        self.remain = capacity
        
    def get(self, key):
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)  # del 掉了
        self.dic[key] = v # key as the newest one
        return v
    
    def put(self, key, value):
        if key in self.dic: # 在里面
            self.dic.pop(key) #删掉这个，再加，新来的就放在最前面了
        else: # 不在里面
            if self.remain>0:   # 还有剩余的
                self.remain -= 1 # 那就直接加进来
            else:
                self.dic.popitem(last=False) # 删除掉第一个
        self.dic[key] = value
        
        # 替换算法
        
# 用双向链表实现的版本：
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    
    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部和伪尾部节点
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail 
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 存在就提到最前面
        node = self.cache[key]
        self.moveToHead(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # if not exists, then create a new node
            node = DLinkedNode(key, value)
            # add to the Hash 
            self.cache[key] = node
            # add to the doublelinklist's head
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # if > volumn, delete the last node
                removed = self.removeTail()
                # del the exact item
                self.cache.pop(removed.key)
                self.size -= 1
            else:
                # key exist, hash->get, then move to the head
                node = self.cache[key]
                node.value = value
                self.moveToHead(node)
                
        def addToHead(self, node):
            node.prev = self.head   # 这里就是把它移到最前面来了。
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            
        def removeNode(self, node):
            node.prev.next = node.next
            node.next.prev = node.prev
            
        def moveToHead(self, node):
            self.removeNode(node)
            self.addToHead(node)
            
        def removeTail(self):
            node = self.tail.prev
            self.removeNode(node)
            return node
            
            
            
            
            
            
            
            
        
        
        
        
        
        
        
        

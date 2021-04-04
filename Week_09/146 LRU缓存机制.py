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
        

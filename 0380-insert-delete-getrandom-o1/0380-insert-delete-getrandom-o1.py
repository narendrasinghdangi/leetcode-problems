class RandomizedSet:

    def __init__(self):
        self.li=set()

    def insert(self, val: int) -> bool:
        if val in self.li:
            return False
        else:
            self.li.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.li:
            self.li.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        lis=list(self.li)
        return random.choice(lis)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
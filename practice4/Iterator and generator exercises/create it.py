class Bes1111:
    def __init__(self,n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        val = self.current
        self.current+=1
        return val
    

for x in Bes1111(5):
    print(x)
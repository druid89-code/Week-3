class IndexedMinPQ:
    def less(self, i, j):
        return self.priorities[i] > self.priorities[j]
    def swap(self, i, j):
        self.values[i],self.values[j] =self.values[j],self.values[i]
        self.priorities[i],self.priorities[j] = self.priorities[j],self.priorities

        self.location[self.values[i]] = i
        self.location[self.values[j]] = j

    def _init_(self, size):
        self.N = 0
        self.size = size
        self.values = [0] * (size + 1)
        self.priorities = [None] * (size + 1)

        self.location = {}
    def _contains_(self, v):
        return v in self.location
    def enqueue(self, v, p):
        self.N += 1

        self.values[self.N], self.priorities[self.N] = v, p
        self.location[v] = self.N
        self.swim(self.N,)
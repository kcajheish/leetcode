class UF:
    def __init__(self, N):
        self.count = N
        self.parent = [ i for i in range(N)]
        self.size = [1 for i in range(N)]

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)

        if root_p == root_q:
            return

        if self.size[p] > self.size[q]:
            self.parent[q] = root_p
        else:
            self.parent[p] = root_q
        self.count -= 1


    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]] #compression
            p = self.parent[p]
        return p

    def count(self):
        return self.count
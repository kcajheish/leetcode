class SegmentTree:
    def __init__(self, arr):
        self.tree = []
        self.arr = arr
    def build(self, node, start, end):
        if start == end:
            self.tree[node] =  self.arr[start]
        else:
            mid = start + (end-start)//2
            self.build(2*node+1, start, mid)
            self.build(2*node+2, mid+1, end)
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def update(self, node, start, end, index, value):
        if start == end:
            self.arr[index] = value
            self.tree[node] = value
        else:
            mid = start + (end-start)//2
            if start <=index and index <= mid:
                self.update(2*node+1, start, mid, index, value)
            else:
                self.update(2*node+2, mid+1, end, index, value)
        self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def query(self, node, start, end, l, r):
        if end < l or start > r:
            return 0
        elif  start >= l and end <= r:
            return self.tree[node]
        else:
            mid = start + (end-start)//2
            left_sum = self.query(2*node+1, start, mid,l, r)
            right_sum = self.query(2*node+2, mid+1, end, l, r)
            return right_sum + left_sum

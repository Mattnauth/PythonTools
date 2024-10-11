import ListMaxHeap

class HeapNode:
    # heap: ListMaxHeap = None
    # index: int = None
    def __init__(self, index:int, heap:ListMaxHeap):
        self.heap: ListMaxHeap = heap
        self.index: int = index

    def left(self):
        if(self.heap.left(self.index) == None):
            return None
        return HeapNode(self.heap.left(self.index), self.heap)
    def right(self):
        if(self.heap.right(self.index) == None):
            return None
        return HeapNode(self.heap.right(self.index), self.heap)
    def value(self):
        return self.heap.key(self.index)
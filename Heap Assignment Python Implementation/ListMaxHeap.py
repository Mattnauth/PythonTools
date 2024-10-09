class ListMaxHeap:
    def __init__(self, initial_values:list = []):
        self.__heap_array:list = []
        for item in initial_values:
            self.__heap_array.append(item)

        self.build_max_heap()
    
    #Internal functions that operate on the list
    def value(self, index:int):
        '''Returns the value at a given index, or None if index is not valid.'''
        if (index == None) or (index < 0) or (index >= self.numItems()):
            return None
        return self.__heap_array[index]
    
    def swap(self,index1:int,index2:int):
        """Swaps the values at the given indices."""
        temp = self.__heap_array[index1]
        self.__heap_array[index1] = self.__heap_array[index2]
        self.__heap_array[index2] = temp

    def numItems(self):
        """Returns the count of elements in the heap"""
        return len(self.__heap_array)
    
    #Heap API functions    
    def array(self):
        '''Returns a copy of the internal list containing all the heap elements.'''
        return self.__heap_array.copy()
    
    def insert(self, element):
        '''Inserts 'element' into the heap and heapifies the heap.'''
        self.__heap_array.append(element)
        self.swap(0, self.numItems()-1)
        self.max_heapify(0)

    def max(self):
        '''Returns the maximum value in the heap.'''
        return self.__heap_array[0]
    
    def remove_max(self):
        '''Removes the maximum value from the heap and validates the heap.'''
        self.swap(0,self.numItems()-1)
        removed_value = self.__heap_array.pop()
        self.max_heapify(0)
        return removed_value
    
    #Navigation functions for moving through the heap as a tree
    def parent(self, child_index:int) -> int:
        """Returns the index of the child's parent. Returns None if child_index is invalid or index is the root."""
        if(child_index == 0 or child_index >= self.numItems()):
            return None
        return (child_index-1)//2
    
    def left(self, parent_index:int) -> int:
        """Returns the index of a parent's left child.  Returns None if there is no left child."""
        index = parent_index*2 + 1
        return index if (index < self.numItems()) else None
    
    def right(self, parent_index:int) -> int:
        """Returns the index of a parent's right child.  Returns None if there is no right child."""
        index = parent_index*2 + 2
        return index if (index < self.numItems()) else None
    
    #Utility functions for managing the heap
    def build_max_heap(self):
        """Runs through the heap in reverse and sinks values to validate the whole max heap.
        Only called once when the heap is initialized from a list."""
        if(self.numItems() == 0):
            return
        for index in range(self.parent(self.numItems()-1), -1, -1):
            self.max_heapify(index)

    def max_heapify(self,index):
        '''Sinks the value at target index until there are no greater values in its children.'''
        target = self.greaterChild(index)
        while(target != None):
            self.swap(index,target)
            index = target
            target = self.greaterChild(index)

    def greaterChild(self, parent_idx) -> int|None:
        '''Returns None if the given index is greater than both children, or does no exist.
        Otherwise returns the index of the greatest child.'''
        left_child_idx, right_child_idx = self.left(parent_idx), self.right(parent_idx)
        values = [
            (self.value(parent_idx), parent_idx),
            (self.value(left_child_idx), left_child_idx),
            (self.value(right_child_idx), right_child_idx),
        ]
        values = [x for x in values if x[0] is not None]
        max_idx = max(values)[1] if len(values) else None

        return None if max_idx == parent_idx else max_idx
        
    #Side effect (e.g print) functions    
    def __str__(self) -> str:
        return str(self.__heap_array)


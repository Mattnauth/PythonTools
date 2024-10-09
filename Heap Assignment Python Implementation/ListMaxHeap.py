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
        return len(self.__heap_array)
    
    #Heap API functions    
    def array(self):
        '''Returns a copy of the internal list containing all the heap elements.'''
        return self.__heap_array.copy()
    
    def insert(self, element):
        '''Inserts 'element' into the heap and heapifies the heap.'''
        self.__heap_array.append(element)
        self.bubble(self.numItems()-1)

    def max(self):
        return self.__heap_array[0]
    
    def removeMax(self):
        self.swap(0,self.numItems()-1)
        removed_value = self.__heap_array.pop()
        self.sink(0)
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
        for index in range(self.parent(self.numItems()-1), -1,-1):
            if(self.greaterChild(index) != None):
                self.sink(index)

    def sink(self,index):
        '''Sinks the value at target index until there are no greater values in its children.
        Generally called on index zero after a remove, to re-validate the heap.'''
        target = self.greaterChild(index)
        while(target != None):
            self.swap(index,target)
            index = target
            target = self.greaterChild(index)

    def bubble(self, index):
        '''Bubbles up the value at target index until there are no lesser values above it.
        Generally called on the last index after an add, to re-validate the heap.'''
        bubble_idx = index
        parent_idx = self.parent(bubble_idx)
        while (parent_idx != None) and (self.value(bubble_idx) > self.value(parent_idx)):
            self.swap(bubble_idx,parent_idx)
            bubble_idx = parent_idx
            parent_idx = self.parent(bubble_idx)

    def greaterChild(self, parent_idx) -> int|None:
        '''Returns None if the given index is greater than both children, otherwise returns the index of the greatest child.'''
        left_child_idx, right_child_idx = self.left(parent_idx), self.right(parent_idx)
        values = [
            (self.value(parent_idx), parent_idx),
            (self.value(left_child_idx), left_child_idx),
            (self.value(right_child_idx), right_child_idx),
        ]
        values = [x for x in values if x[0] is not None]
        min_idx = min(values)[1]

        return None if min_idx == parent_idx else min_idx
        if(left_child_id != None and right_child_idx != None):
            #Case where both children exist, check if either is greater than the other and index (parent)
            if(self.value(left_child_id) >= self.value(right_child_idx) and self.value(left_child_id) > self.value(parent_idx)):
                return left_child_id
            elif(self.value(right_child_idx) >= self.value(left_child_id) and self.value(right_child_idx) > self.value(parent_idx)):
                return right_child_idx
            else:
                #If neither child is greater, return None
                return None
        elif(left_child_id != None and self.value(left_child_id) > self.value(parent_idx)):
            #Case where left child exists and is greater than index (parent)
            return left_child_id
        elif(right_child_idx != None and self.value(right_child_idx) > self.value(parent_idx)):
            #Case where right child exists and is greater than index (parent)
            return right_child_idx
        else:
            #Case where neither child exists or neither child is less than index, return None
            return None
        
    #Side effect (e.g print) functions    
    def __str__(self) -> str:
        return str(self.__heap_array)


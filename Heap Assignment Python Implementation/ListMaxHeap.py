class ListMaxHeap:
    def __init__(self, initial_elements:list = [], element_to_key = None):
        '''Creates a max-heap from the supplied list of initial elements
        (or an empty heap if the list is empty).
        Optional: element_to_key function may be supplied that takes the
        element and returns its key (otherwise elements will be compared directly).'''
        self.element_to_key = element_to_key
        self.__heap_array:list = []
        for item in initial_elements:
            self.__heap_array.append(item)

        self.build_max_heap()
    
    #Internal functions that operate on the list
    def key(self, index:int):
        '''Returns the key of the object at a given index, or None if index is not valid.'''
        if (index == None) or (index < 0) or (index >= self.numItems()):
            return None
        if self.element_to_key != None:
            return self.element_to_key(self.__heap_array[index])
        return self.__heap_array[index]
    
    def swap(self,index1:int,index2:int):
        """Swaps the objects at the given indices."""
        self.__heap_array[index1], self.__heap_array[index2] =\
            self.__heap_array[index2], self.__heap_array[index1]

    def numItems(self) -> int:
        '''Returns the number of items in the heap.'''
        return len(self.__heap_array)

    def lastIndex(self) -> int|None:
        '''Returns the index of the last item in the heap, or None the heap is empty.'''
        return self.numItems()-1 if self.numItems() > 0 else None 
    
    #Heap API functions    
    def array(self):
        '''Returns a copy of the internal list containing all the heap elements.'''
        return self.__heap_array.copy()
    
    def max_heap_insert(self, element):
        '''Inserts new object 'element' into the heap and validates the heap.'''
        self.__heap_array.append(element)
        self.max_heap_validate_idx(self.lastIndex())

    def max(self):
        '''Returns the object with the max key in the heap, without removing it.'''
        return self.__heap_array[0]
    
    def removeMax(self):
        '''Removes and returns the object with the max key in the heap and validates the heap.'''
        self.swap(0,self.numItems()-1)
        max = self.__heap_array.pop()
        self.max_heapify(0)
        return max
    
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
        for index in range(self.parent(self.lastIndex()), -1,-1):
            if(self.greaterChild(index) != None):
                self.max_heapify(index)

    def max_heapify(self,index):
        '''Sinks the value at target index until there are no greater values in its children.
        Generally called on index zero after a remove, to re-validate the heap.'''
        target_idx = self.greaterChild(index)
        while(target_idx != None):
            self.swap(index,target_idx)
            index = target_idx
            target_idx = self.greaterChild(index)


    def max_heap_validate_idx(self, target_idx):
        '''Should be called when the element at the target index has been changed or added.
        Re-checks the key of the element at the target index and
        heapifies or bubbles up the element if/as needed to re-validate the heap.'''
        parent_idx = self.parent(target_idx)
        if (parent_idx != None) and (self.key(target_idx) > self.key(parent_idx)):
            while (parent_idx != None) and (self.key(target_idx) > self.key(parent_idx)):
                self.swap(target_idx,parent_idx)
                target_idx = parent_idx
                parent_idx = self.parent(target_idx)
        else:
            self.max_heapify(target_idx)

    def greaterChild(self, parent_idx) -> int|None:
        '''Returns None if the given index is greater than both children, otherwise returns the index of the greatest child.'''
        left_child_idx = self.left(parent_idx)
        right_child_idx = self.right(parent_idx)
        keys = [
            (self.key(parent_idx), parent_idx),
            (self.key(left_child_idx), left_child_idx),
            (self.key(right_child_idx), right_child_idx),
        ]
        keys = [x for x in keys if x[0] is not None]
        max_idx = None
        max_idx = max(keys)[1] if len(keys) > 0 else None

        return None if max_idx == parent_idx else max_idx
        
    #Side effect (e.g print) functions    
    def __str__(self) -> str:
        return str(self.__heap_array)


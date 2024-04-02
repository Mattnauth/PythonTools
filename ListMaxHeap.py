import math
import BinaryTreeUtils

class ListMaxHeap:
    def __init__(self, initial_values:list = []):
        self.__heap_array:list = []
        for item in initial_values:
            self.__heap_array.append(item)

        self.heapify()
    
    #Internal functions that operate on the list
    def value(self, index:int):
        '''Returns the value at a given index, or NOne if index is not valid.'''
        if (index == None) or (index < 0) or (index > self.numItems()):
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
        return self.__heap_array.copy()
    
    def insert(self, value):
        self.__heap_array.append(value)
        self.bubble(self.numItems()-1)

    def max(self):
        return self.__heap_array[0]
    
    def removeMax(self):
        removed_value = self.__heap_array[0]
        self.swap(0,self.numItems()-1)
        self.sink(0)
        return removed_value
    
    #Navigation functions for moving through the heap as a tree
    def parent(self, child_index:int) -> int:
        """Returns the index of the child's parent. Returns None if child_index is invalid or index is the root."""
        index = (child_index-1)//2
        return index if (index < self.numItems() and index >= 0) else None
    
    def left(self, parent_index:int) -> int:
        """Returns the index of a parent's left child.  Returns None if there is no left child."""
        index = parent_index*2 + 1
        return index if (index < self.numItems()) else None
    
    def right(self, parent_index:int) -> int:
        """Returns the index of a parent's right child.  Returns None if there is no right child."""
        index = parent_index*2 + 2
        return index if (index < self.numItems()) else None
    
    #Utility functions for managing the heap
    def heapify(self):
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
        target = self.parent(index)
        while(target != None and self.value(index) > self.value(target)):
            self.swap(index,target)
            index = target
            target = self.parent(index)

    def greaterChild(self, index) -> int|None:
        '''Returns None if the given index is greater than both children, otherwise returns the index of the greatest child.'''
        left = self.left(index)
        right = self.right(index)
        if(left != None and right != None):
            #Case where both children exist, check if either is greater than the other and index (parent)
            if(self.value(left) >= self.value(right) and self.value(left) > self.value(index)):
                return left
            elif(self.value(right) >= self.value(left) and self.value(right) > self.value(index)):
                return right
            else:
                #If neither child is greater, return None
                return None
        elif(left != None and self.value(left) > self.value(index)):
            #Case where left child exists and is greater than index (parent)
            return left
        elif(right != None and self.value(right) > self.value(index)):
            #Case where right child exists and is greater than index (parent)
            return right
        else:
            #Case where neither child exists or neither child is less than index, return None
            return None
        
    #Side effect (e.g print) functions    
    def __str__(self) -> str:
        return str(self.__heap_array)

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
        return self.heap.value(self.index)

if __name__ == "__main__":
    def testHeap(initial_values:list):
        print("Testing heap creation with initial elements:", initial_values)
        test_heap = ListMaxHeap(initial_values)
        print("Array view of test heap:")
        print(test_heap)
        print("Tree view of test heap:")
        BinaryTreeUtils.printTreeDiagramFromLTRArray(test_heap.array())
        BinaryTreeUtils.printTreeDiagram(HeapNode(0,test_heap))
        print("Number of Elements in test_heap is:", test_heap.numItems())
        print("Count() of root of test_heap is:", BinaryTreeUtils.count(HeapNode(0,test_heap)))
        

    def listen(target_heap:ListMaxHeap):
        user_input = ''
        exit_flag = False
        while(not exit_flag):
            user_input = input()
            user_input_array = user_input.split(" ")
            match user_input_array[0]:
                case "add":
                    if len(user_input_array) < 1:
                        break
                    target_heap.insert(user_input_array[1])
                    print(f"Added {user_input_array[1]}, new heap diagram after bubbling:")
                    BinaryTreeUtils.printTreeDiagram(HeapNode(0,target_heap))
                case "remove":
                    return_value = target_heap.removeMax()
                    print(f"Removed {return_value}, new tree heap diagram after sinking:")
                    BinaryTreeUtils.printTreeDiagram(HeapNode(0,target_heap))
                case "print":
                    BinaryTreeUtils.printTreeDiagram(HeapNode(0,target_heap))
                case "note:":
                    pass
                case "exit":
                    exit_flag = True

    # testHeap([])
    #testHeap([92, 48, 94, 37, 32, 76, 14, 84, 50, 79])
    print("Heap Visualizer V1.0 by Matthew Nauth written in Python 3.11.4")
    print("Commands: Add [int], Remove, Print, Note: [str], Exit")
    heap:ListMaxHeap = ListMaxHeap([])
    listen(heap)


import ListMaxHeap as LMH
import HeapNode as HN
import BinaryTreeUtils

if __name__ == "__main__":
    def testHeap(initial_values:list):
        print("Testing heap creation with initial elements:", initial_values)
        test_heap = LMH.ListMaxHeap(initial_values)
        print("Array view of test heap:")
        print(test_heap)
        print("Tree view of test heap:")
        BinaryTreeUtils.printTreeDiagramFromLTRArray(test_heap.array())
        BinaryTreeUtils.printTreeDiagram(LMH.HeapNode(0,test_heap))
        print("Number of Elements in test_heap is:", test_heap.numItems())
        print("Count() of root of test_heap is:", BinaryTreeUtils.count(LMH.HeapNode(0,test_heap)))
        

    def listen(target_heap:LMH.ListMaxHeap):
        user_input = ''
        exit_flag = False
        while(not exit_flag):
            print("Enter command: ", end='')
            user_input = input().strip()
            user_input_array = user_input.split(" ")
            if len(user_input_array) > 1:
                try:
                    user_input_array[1] = int(user_input_array[1])
                except:
                    user_input_array = user_input_array[:1]
            match user_input_array[0]:
                case "add":
                    if (len(user_input_array) > 1) and (type(user_input_array[1]) == int):
                        target_heap.insert(user_input_array[1])
                        print(f"Added {user_input_array[1]}, new tree diagram of heap after bubbling:")
                        BinaryTreeUtils.printTreeDiagram(HN.HeapNode(0,target_heap))
                case "remove":
                    return_value = target_heap.remove_max()
                    print(f"Removed {return_value}, new tree diagram of heap after sinking:")
                    BinaryTreeUtils.printTreeDiagram(HN.HeapNode(0,target_heap))
                case "print":
                    BinaryTreeUtils.printTreeDiagram(HN.HeapNode(0,target_heap))
                case "note:":
                    pass
                case "exit":
                    exit_flag = True
                # case "parent":
                #     print(target_heap.parent(user_input_array[1]))

    # testHeap([])
    #testHeap([92, 48, 94, 37, 32, 76, 14, 84, 50, 79])
    print("Heap Visualizer V1.0 by Matthew Nauth written in Python 3.11.4")
    print("Commands: Add [int], Remove, Print, Note: [str], Exit")
    heap:LMH.ListMaxHeap = LMH.ListMaxHeap([])
    listen(heap)
import math

def count(node) -> int:
    """Recursively counts the number of nodes in a binary tree rooted at node."""
    if(node == None):
        return 0
    return count(node.left()) + count(node.right()) + 1

def height(node) -> int:
    """Recursively determines the height of a binary tree rooted at node."""
    if(node == None):
        return 0
    return max(height(node.left()), height(node.right())) + 1


def insertStringAtIndex(index: int, s: str, insert:str) -> str:
    """Takes string s and returns a copy with string insert overwritten, centered at index."""
    left_chars = round(len(insert)/2)
    left_idx = index - left_chars
    return s[:left_idx] + insert + s[left_idx+len(insert):]  

def printTreeDiagram(root):
    """Takes a binary tree node object that must support left(), right(), and value() methods.
    left() must return the left child node of the node or None
    right() must return the right child node of the node or None
    value() must return the value of the node"""
    ltr_array = []
    leftToRightTraversal(root, ltr_array)
    printTreeDiagramFromLTRArray(ltr_array)

def printTreeDiagramFromLTRArray(array:list):
    """Takes a left-to-right, level-by-level list of nodes in a binary tree structure and
    prints a tree diagram to the console. Values are surrounded by parenthesis to indicate a node,
    and slashes roughly indicate connecting edges. Values of none in the array will be renderd as blank spaces
    surrounded by parenthesis."""
    trimmed_array = [item for item in array if item != None]
    array = ["" if item == None else item for item in array]

    num_items = len(array)
    if num_items < 1:
        print("Tree diagram is empty.")
        print("Array View:",array)
        return
    #Figure the number of levels required for the tree diagram (1-based indexing)
    num_levels = math.floor(math.log2(num_items))+1

    #Get a list of items in the last level
    last_level_list = array[(2**(num_levels-1))-1:]
    last_level_str_lengths = [len(str(i)) for i in last_level_list]

    #Calculate the width of a "block" to use for displaying one value based on the longest string (with some padding)
        #Note we only care about the width of items in the last level because they're mashed closest together.
    max_num_width = max(last_level_str_lengths)
    padding = 1
    max_str_width = max_num_width + padding

    #Calculate the total width required for to display the last level, assuming it's full.
    #(Number of items in a level * width)
    total_width = ((2**num_levels)*(max_str_width))

    #Bump the lowest level width up to the nearest multiple of two
    #total_width = 2**(math.ceil(math.log2(total_width)))

    for level in range(num_levels):
        start_index = 2**(level)-1
        num_elems = 2**level
        field_width = int(total_width / num_elems)
        next_field_width = int(total_width/(num_elems*2))

        #Print the elements for a level
        element_layer: str = " "*total_width
        string_target_index = round(field_width/2)
        for j in range(start_index, start_index+num_elems):
            if(j < num_items):
                element_layer = insertStringAtIndex(string_target_index,element_layer,
                                                    "("+str(array[j]).rjust(max_num_width," ")+")")
                #print(str(array[j]).center(field_width),end='')
            string_target_index += field_width
        print(element_layer)

        #Print connecting slashes for level below
        if(level == num_levels - 1):
            break
        sep_layer: str = " "*total_width
        for j2 in range(0,num_elems):
            indent: int = j2*field_width
            left_slash_idx: int = round((field_width/2 + next_field_width/2)/2 + indent)-1
            sep_layer = insertStringAtIndex(left_slash_idx,sep_layer,"/")
            right_slash_idx: int = round((field_width/2 + next_field_width*1.5)/2 + indent)
            sep_layer = insertStringAtIndex(right_slash_idx,sep_layer,"\\")
        print(sep_layer)

    print("Array:",trimmed_array)

def leftToRightTraversal(root, array:list):
    """Creates a left-to-right, level-by-level array of values for a binary tree rooted at root.  
    Empty nodes will be inserted into the array with value None 
    to form a complete binary tree based on the root's height.
    Root node object must support .left() .right() and .value() methods which return left/right child nodes
    and the value of the node, respectively."""
    levels = height(root)
    array.append(root)
    level_start_index = 0
    for i in range(1,levels):
        items_in_level = 2**(i-1)
        level_end_index = level_start_index + items_in_level
        for j in range(level_start_index,level_end_index):
            array.append(None if array[j] == None else array[j].left())
            array.append(None if array[j] == None else array[j].right())
        level_start_index += items_in_level
    
    for index in range(len(array)):
        array[index] = None if array[index] == None else array[index].value()
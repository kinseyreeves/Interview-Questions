"""
Binary-tree implementation with different functionality.
for reference.

Kinsey Reeves
"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert_node(element, tree):
    #print(tree.data)
    if(element <= tree.data):
        #print("less")
        if(tree.left):
            insert_node(element,tree.left)
        else:
            tree.left = Node(element)
    else:
        #print("right")
        if(tree.right):
            insert_node(element, tree.right)
        else:
            tree.right = Node(element)

def in_order_print_tree(tree):
    if(tree):
        in_order_print_tree(tree.left)
        print(tree.data, end='')
        in_order_print_tree(tree.right)
        
def create_tree(lst):
    root = Node(lst[0])
    for i in lst[1:]:
        #print("inserted")
        insert_node(i, root)
    return root

def print_depth(tree):
    print("tree depth: ")
    print(_depth(tree))

def _depth(tree):
    if(not tree):
        return 0
    if(_depth(tree.left) > _depth(tree.right)):
        return _depth(tree.left) + 1
    return _depth(tree.right) + 1


def size(tree):
    if not tree:
        return 0
    else:
        return size(tree.left) + size(tree.right) + 2

def is_balanced(tree):
    if not tree:
        return True
    if abs(_depth(tree.left) - _depth(tree.right)) <= 1:
        return is_balanced(tree.left) and is_balanced(tree.right)
    return False

def print_levels(tree):
    print('',end='')
    open_set = set()
    open_set.add(tree)
    while len(open_set) > 0:
        t = open_set.pop()
        print(t.data, end = ' ')
        if(t.left):
            open_set.add(t.left)
        if(t.right):
            open_set.add(t.right)
    print('\n')

def print_structure(tree):
    if(tree):
        return f'[ {tree.data} ' + f'{print_structure(tree.left)} ' + f' {print_structure(tree.right)}]'
    else:
        return 'Nil'
        

t = create_tree([1,2,1,4,5,2])
in_order_print_tree(t)
print('\n')
print_levels(t)
print_depth(t)
print(is_balanced(t))
print_levels(t)
#in_order_print_tree(t)

print(print_structure(t))



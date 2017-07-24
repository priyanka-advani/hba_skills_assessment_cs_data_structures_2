# --------- #
# Recursion #
# --------- #

# 1. Write a function that uses recursion to print each item in a list.
def print_item(my_list, i=0):
    """Prints each item in a list recursively.

        >>> print_item([1, 2, 3])
        1
        2
        3

        >>> print_item([])

    """
    
    # base case: stop once there are no items left to print
    if i >= len(my_list):
        return

    # print item at index, recurse with incremented index
    print my_list[i]
    print_item(my_list, i + 1)


# 2. Write a function that uses recursion to print each node in a tree.

def print_all_tree_data(tree):
    """Prints all of the nodes in a tree.


        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> print_all_tree_data(one)
        1
        2
        3

    """
    
    # base case: stop once tree == None
    if not tree:
        return

    # print tree data
    else:
        print tree.data

    # loop over children list & print each child recursively
    for child in tree.children:
        print_all_tree_data(child)


# 3. Write a function that uses recursion to find the length of a list.


def list_length(my_list):
    """Returns the length of list recursively.
        >>> list_length([1, 2, 3, 4])
        4

    """

    # base case: length of an empty list is 0
    if not my_list:
        return 0

    # if there are items in the list, add one (for the first element)
    # and recurse on the remainder of the list
    else:
        return list_length(my_list[1:]) + 1


# 4. Write a function that uses recursion to count how many nodes are in a tree.

def num_nodes(tree):
    """Counts the number of nodes.

        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> num_nodes(one)
        3
        >>> four = Node(4)
        >>> five = Node(5)
        >>> two.add_child(four)
        >>> two.add_child(five)
        >>> num_nodes(one)
        5
        >>> six = Node(6)
        >>> three.add_child(six)
        >>> num_nodes(one)
        6
    """

    # base case: if tree == None, pass 0 back to the previous call
    if not tree:
        return 0

    # count nodes in children recursively
    else:
        total_nodes = 0

        for child in tree.children:
            total_nodes += num_nodes(child)

    # add 1 to total for the original node
    return total_nodes + 1


#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

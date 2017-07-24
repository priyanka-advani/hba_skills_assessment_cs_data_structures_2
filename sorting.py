#Sorting

def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    
    # stop iterating one before the end (no more pairs to compare)
    for i in range(len(lst) - 1):

        # set swapped variable to False, only change to True when a swap is made
        swapped = False

        # subtract index to avoid re-checking items we have already sorted
        for j in range(len(lst) - 1 - i):

            # if item is greater than next item, swap their incides
            # & set swapped variable to True
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True

        # if no swap is made, break out of the loop
        if not swapped:
            break

    return lst


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    # new list to store sorted items
    sorted_list = []

    # break loop as soon as one list is empty
    while len(list1) > 0 and len(list2) > 0:

        # compare first item in each list, pop smaller item & append to new list
        if list1[0] < list2[0]:
            sorted_list.append(list1.pop(0))

        else:
            sorted_list.append(list2.pop(0))

    # extend the new list with the remaining items from both lists
    # (one will be empty)
    sorted_list.extend(list1)
    sorted_list.extend(list2)

    return sorted_list


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.

    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.

    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
    
    # list with 1 item in it is already sorted
    if len(lst) < 2:
        return lst

    # index at midpoint of the list
    midpoint = len(lst) / 2

    # call merge_sort recursively with the 2 halves of the list,
    # breaking them down until the length of each half is 1,
    # at which point they will start returning
    lst1 = merge_sort(lst[:midpoint])
    lst2 = merge_sort(lst[midpoint:])

    # use merge_lists function to merge already-sorted lists
    return merge_lists(lst1, lst2)


#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

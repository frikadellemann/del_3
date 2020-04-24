# Emil Blarke (eblar19) and Mads Frederik Larsen (madla15)
import math

# Here we define some lambda functions,
# that we use as shortcuts for finding 
# the left child, right child or parent of index ‘i’.

left = lambda i: 2 * i + 1
right = lambda i: 2 * i + 2
parent = lambda i: math.floor((i - 1) / 2)

# current heap size can be found via the len() method, 
# therefore we don't need to keep track of the size.
# here we define our insert(A, e) method
# it adds an element to the end of the Heap
# if the new element violates the min-heap structure it will be moved up with
# the move_upwards method, e.g. if the new element is the smallest element


def insert(A, e):
    A.append(e)
    move_upwards(A,len(A)-1)

#  move_upwards compares the item at the index with its parent 
# and swaps them, if it’s smallest.
# stops when we reach the root

def move_upwards(A, index):
    while A[parent(index)] > A[index] and parent(index)>=0:
        swap(A,index,parent(index))
        index = parent(index)


# this method returns the index of the smallest child
# if it has no children it will return index again
# if left index is out of range then left is smallest
# since our parent operator works on math.floor
#  ( i - 1) / 2 for i = 0, 0 - 1 = -1 / 2 = -0,5 math.floor -> -1
# and since (1 - 1) / 2 = 0 math.floor isn’t going to round it
# since floor takes a float / double type and rounds it down to nearest integer
def min_child(A, index):
    l = left(index)
    r = right(index)
    if l < len(A):
        smallest = l
    else:
        smallest = index
    if r < len(A) and A[r] < A[l]:
        smallest = r
    
    return smallest

# We define a method for swapping the values in two indexes with eachother.

def swap(A, pos1, pos2):
    temp = A[pos1]
    A[pos1] = A[pos2]
    A[pos2] = temp


#  Here we define our extractMin() method which:
# replaces the root with the last item in the list
# and returns the former root

def extractMin(A):
    min_val = A[0]
    A[0] = A[-1]
    A.pop()
    move_down(A, 0)
    return min_val

# move_down compares the item at the index with its smallest child
# if the smallest child is less than item it swaps
# it continues with the next index which it swapped with

def move_down(A, index):
    while left(index) < len(A):
        smallest = min_child(A,index)
        if A[index] > A[smallest]:
            swap(A, smallest, index)
        index = smallest





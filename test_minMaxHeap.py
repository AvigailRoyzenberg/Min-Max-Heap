import pytest

from minMaxHeap import *

# UTILITY FUNCTION:
def insertInto_MinMaxHeap(heap, size, rememberInsertions = False):
    insertions = []
        
    for i in range(size):
        randomInt = random.randint(0, 10000)
        randomKey = chr(ord('A') + 1 + i)
        heap.insert(randomInt, randomKey)   # insert size number of random elements
        if rememberInsertions:              # if we want to remember a list of what was inserted
            insertions.append(randomInt)    # add it to the list
    
    if rememberInsertions:
        return insertions                   # return the list of elements inserted


# PYTESTS:

# INSERTION TESTS:

# Insert on a tiny heap:   
def test_tinyInsert():
    h = minMaxHeap(10)        # make a new heap with maximum of 10 elements
    h.insert(1, "A")
    h.insert(2, "B")
    h.insert(3, "C")
    h.insert(100, "D")
    h.insert(4, "E")
    h.insert(2.5, "F")
    assert h.lenHeap() == 6   # check that the length of it is how many were inserted
    assert h.findMax() == 100
    assert h.findMin() == 1
   
    
# Insert on a small heap:   
def test_smallInsert():
    size = 50
    h = minMaxHeap(size)           # make a new heap with size number of elements
    insertInto_MinMaxHeap(h, size) # insert size number of keys/data
    assert h.lenHeap() == size     # check that all were inserted


# Insert on a big heap:   
def test_largeInsert():
    size = 1000
    h = minMaxHeap(size)     
    insertInto_MinMaxHeap(h, size, True)
    assert h.lenHeap() == size
    
    
# Insertion more on a full heap:
def test_insertOnFullHeap():
    size = 100
    h = minMaxHeap(size)                 # make a new heap with size number of elements
    insertInto_MinMaxHeap(h, size-1 )    # insert one less than the full heap size
    assert h.lenHeap() == size-1
                                         # insert one more
    assert h.insert(20, "A") == True     # inserting 1 more, up to size works
    assert h.insert(30, "B") == False    # inserting 1 more than size, fails
    

# FINDMIN TESTS:

# Find min on an empty heap:
def test_findMinEmptyHeap():
    size = 0
    h = minMaxHeap(size) 
    insertInto_MinMaxHeap(h, size)
    assert h.lenHeap() == size
    assert h.findMin() == None      # there should be no min
    
# Find max on a heap of two elements:
def test_findMinOfTwo():
    size = 2
    h = minMaxHeap(size) 
    listOfKeys = insertInto_MinMaxHeap(h, size, True)
    assert h.lenHeap() == size
    assert h.findMin() == min(listOfKeys)  # the min should be the min key of the returned list
    

# Find min on a tiny heap:   
def test_tinyFindMin():
    h = minMaxHeap(10)  # make a new heap with maximum of 31 elements
    h.insert(2, "B")
    h.insert(3, "C")
    h.insert(100, "D")
    h.insert(4, "E")
    h.insert(2.5, "F")  
    h.insert(1, "A")
    assert h.findMin() == 1   
    h.removeMin()
    assert h.findMin() == 2

# Find min on a small heap:
def test_findMinSmallHeap():
    size = 50
    h = minMaxHeap(size) 
    listOfKeys = insertInto_MinMaxHeap(h, size, True)
    assert h.lenHeap() == size
    assert h.findMin() == min(listOfKeys) # the min should be the min key that was inserted into the heap
    
    
# Find min on big heap:
def test_findMinLargeHeap():
    size = 1000
    h = minMaxHeap(size) 
    listOfKeys = insertInto_MinMaxHeap(h, size, True)
    assert h.lenHeap() == size
    assert h.findMin() == min(listOfKeys)  # the min should be the min key that was inserted into the heap

# FINDMAX TESTS:

# Find max on an empty heap:
def test_findMaxEmptyHeap():
    size = 0
    h = minMaxHeap(size) 
    insertInto_MinMaxHeap(h, size)
    assert h.lenHeap() == size
    assert h.findMax() == None
    
    
# Find max on a heap of two elements:
def test_findMaxOfTwo():
    size = 2
    h = minMaxHeap(size) 
    listOfKeys = insertInto_MinMaxHeap(h, size, True)
    assert h.lenHeap() == size
    assert h.findMax() == max(listOfKeys)  # the max should be the max key of the returned list


# Find max on a tiny heap:
def test_tinyFindMax():
    h = minMaxHeap(10)  # make a new heap with maximum of 31 elements
    h.insert(1, "A")
    h.insert(2, "B")
    h.insert(3, "C")
    h.insert(100, "D")
    h.insert(4, "E")
    h.insert(2.5, "F")    
    assert h.findMax() == 100
    h.removeMax()
    assert h.findMax() == 4
    
    
# Find max on a small heap:
def test_findMaxSmallHeap():
    size = 50
    h = minMaxHeap(size) 
    listOfKeys = insertInto_MinMaxHeap(h, size, True) # insert keys and remember and return a list of the insertions
    assert h.lenHeap() == size
    assert h.findMax() == max(listOfKeys)             # the max should be the max key of the returned list


# Find max on a big heap:
def test_findMaxLargeHeap():
    size = 1000
    h = minMaxHeap(size) 
    listOfKeys = insertInto_MinMaxHeap(h, size, True)
    assert h.lenHeap() == size
    assert h.findMax() == max(listOfKeys)             # the max should be the max key of the returned list
    

# REMOVE MIN TESTS:

# RemoveMin on an empty heap:
def test_removeMinOfEmptyHeap():
    size = 0
    h = minMaxHeap(size) 
    insertInto_MinMaxHeap(h, size)
    assert h.lenHeap() == size    
    assert h.removeMin() == (None, None)   # heap should be empty
    

# RemoveMin on a heap of one element
def test_removeMinOfSize1():
    size = 1
    h = minMaxHeap(size) 
    insertInto_MinMaxHeap(h, size)
    assert h.lenHeap() == size             # first length should be 1
    remove = h.removeMin()                 # after removal
    assert h.lenHeap() == 0                # check that the heap is now empty
    

# RemoveMin on a small heap:
def test_smallRemoveMin():
    size = 50
    h = minMaxHeap(size) 
    listOfKeys = insertInto_MinMaxHeap(h, size, True)
    assert h.lenHeap() == size             # check the length BEFORE remove -> 50
    assert h.findMin() == min(listOfKeys)  # make sure the min is the min of the heap
    
    minKey = min(listOfKeys)
    
    # count how many time this key appeared in the list
    # if it occured more than once we know that we can't test to see
    # if the old min equal the new min's after removal
    
    multiplesOfMinKey = 0
    for c in listOfKeys:
        if c == minKey:
            multiplesOfMinKey += 1
            if multiplesOfMinKey == 2:
                break    
    
    h.removeMin()                      # remove 1 element, the min
    assert h.lenHeap() == size-1       # check the length AFTER remove - should be 1 less than the original size
    if multiplesOfMinKey != 2:         # if there aren't any repetitions of the minKey in the original heap
        assert h.findMin() != minKey   # the new min should not be equal to the old min    


# RemoveMin on a big heap:
def test_largeRemoveMin():
    size = 10000
    h = minMaxHeap(size) 
    listOfKeys = insertInto_MinMaxHeap(h, size, True)
    assert h.lenHeap() == size              # check the length BEFORE remove -> 10000
    assert h.findMin() == min(listOfKeys)   # make sure the min is the min of the heap
    
    minKey = min(listOfKeys)
    
    # count how many time this key appeared in the list
    # if it occured more than once we know that we can't test to see
    # if the old min equals the new min after removal
    
    multiplesOfMinKey = 0
    for c in listOfKeys:
        if c == minKey:
            multiplesOfMinKey += 1
            if multiplesOfMinKey == 2:
                break
            
    h.removeMin()                      # remove 1 element, the min
    assert h.lenHeap() == size-1       # check the length AFTER remove - should be 1 less than the original size
   
    if multiplesOfMinKey != 2:         # if there aren't any repetitions of the minKey in the original heap
        assert h.findMin() != minKey   # the new min should not be equal to the old min


# RemoveMin several times in a row:
def test_severalRemoveMins():
    size = 100
    h = minMaxHeap(size) 
    listOfKeys = insertInto_MinMaxHeap(h, size, True)    
    assert h.findMin() == min(listOfKeys)
    min1 = min(listOfKeys)                # get the min of the keys inserted
    h.removeMin()                         # remove it from the heap
    listOfKeys.remove(min1)               # remove it from the tracking list
    
    assert h.findMin() == min(listOfKeys) # check that the new min of the tracking list = new min of the heap
    
    min2 = min(listOfKeys)                # get the new min of the keys inserted
    h.removeMin()                         # remove it from the heap
    listOfKeys.remove(min2)               # remove it from the tracking list    
    
    assert h.findMin() == min(listOfKeys) # check that the new min of the tracking list = new min of the heap
    
    min3 = min(listOfKeys)                # get the new min of the keys inserted
    h.removeMin()                         # remove it from the heap
    listOfKeys.remove(min3)               # remove it from the tracking list
    
    assert h.findMin() == min(listOfKeys) # check that the new min of the tracking list = new min of the heap


# REMOVEMAX TESTS:

# RemoveMax of an empty Heap:
def test_removeMaxOfEmptyHeap():
    size = 0
    h = minMaxHeap(size) 
    insertInto_MinMaxHeap(h, size)
    assert h.lenHeap() == size    
    assert h.removeMax() == (None, None)   # check that the heap is empty
    

# RemoveMax of a heap with one element:
def test_removeMaxOfSize1():
    size = 1
    h = minMaxHeap(size) 
    insertInto_MinMaxHeap(h, size)
    assert h.lenHeap() == size             # check length before -> 1
    remove = h.removeMax()
    assert h.lenHeap() == 0                # check that the heap is now length 0 -> empty
    
    
# RemoveMax on a small heap:
def test_smallRemoveMax():
    size = 50
    h = minMaxHeap(size) 
    listOfKeys = insertInto_MinMaxHeap(h, size, True)
    assert h.lenHeap() == size             # check the length BEFORE remove -> 50
    assert h.findMax() == max(listOfKeys)  # make sure the max is the max of the heap
    
    maxKey = max(listOfKeys)
    
    # count how many time this key appeared in the list
    # if it occured more than once we know that we can't test to see if the
    # old max equal the new maxs after removal
    
    multiplesOfMaxKey = 0
    for c in listOfKeys:
        if c == maxKey:
            multiplesOfMaxKey += 1
            if multiplesOfMaxKey == 2:
                break    
    
    h.removeMax()                      # remove 1 element, the max
    assert h.lenHeap() == size-1       # check the length AFTER remove - should be 1 less than the original size
    
    # sometimes, if the max number was randomly inserted again, we can do this assertion:
    if multiplesOfMaxKey != 2:         # if there aren't any repetitions of the maxKey in the original heap
        assert h.findMax() != maxKey   # the new max should not be equal to the old max    


# RemoveMax on a big heap:
def test_largeRemoveMax():
    size = 10000
    h = minMaxHeap(size) 
    listOfKeys = insertInto_MinMaxHeap(h, size, True)
    assert h.lenHeap() == size              # check the length BEFORE remove is size
    assert h.findMax() == max(listOfKeys)   # make sure the max is the max of the heap
    
    maxKey = max(listOfKeys)
    
    # count how many time this key appeared in the list
    # if it occured more than once we know that we can't test to see if the
    # old max equal the new maxs after removal
    
    multiplesOfMaxKey = 0
    for c in listOfKeys:
        if c == maxKey:
            multiplesOfMaxKey += 1
            if multiplesOfMaxKey == 2:
                break
            
    h.removeMax()                      # remove 1 element, the max
    assert h.lenHeap() == size-1       # check the length AFTER remove - should be 1 less than the original size
   
    if multiplesOfMaxKey != 2:         # if there aren't any repetitions of the maxKey in the original heap
        assert h.findMax() != maxKey   # the new max should not be equal to the old max
        

# RemoveMax several times in a row:
def test_severalRemoveMaxes():
    size = 100
    h = minMaxHeap(size) 
    listOfKeys = insertInto_MinMaxHeap(h, size, True)    
    assert h.findMax() == max(listOfKeys)
    max1 = max(listOfKeys)                # get the max of the keys inserted
    h.removeMax()                         # remove it from the heap
    listOfKeys.remove(max1)               # remove it from the tracking list
    
    assert h.findMax() == max(listOfKeys) # check that the new max of the tracking list = new max of the heap
    
    max2 = max(listOfKeys)                # get the new max of the keys inserted
    h.removeMax()                         # remove it from the heap
    listOfKeys.remove(max2)               # remove it from the tracking list    
    
    assert h.findMax() == max(listOfKeys) # check that the new max of the tracking list = new max of the heap
    
    max3 = max(listOfKeys)                # get the new max of the keys inserted
    h.removeMax()                         # remove it from the heap
    listOfKeys.remove(max3)               # remove it from the tracking list
    
    assert h.findMax() == max(listOfKeys) # check that the new max of the tracking list = new max of the heap
    

# Test heapSort propety works on minMaxHeap:
def test_heapSort():
    h = minMaxHeap(100)
    randomInts = [2, 77, 8, 44, 22, 91, 2, 8, 4, 1000, 2555, 63] # random unordered list
    
    for num in randomInts:           # insert it into the heap
        h.insert(num, "A")
    
    orderedList = []
    while h.lenHeap() > 0:
        key, value = h.removeMin()   # keep removing the min
        orderedList.append(key)      # and adding it, in order to the list
    flag = 0
    if (orderedList == sorted(orderedList)): # if our remove works, then the list should now be sorted
        flag = 1
    assert flag == True


def test_randomTortureTest():
    h = minMaxHeap(1000)
    size = 100
    h = minMaxHeap(size) 
    listOfKeys = insertInto_MinMaxHeap(h, size, True)   
    assert h.lenHeap() == size
    maxKey = max(listOfKeys)
    minKey = min(listOfKeys)
    
    assert maxKey == h.findMax()
    assert minKey == h.findMin()
    
    for i in range(20):
        h.removeMin()
    assert h.lenHeap() == size-20
    
    insertInto_MinMaxHeap(h, 20) # insert random 20 elements into heap
    assert h.lenHeap() == size
    
    for i in range(size+20):     # remove more than possible
        ans = h.removeMin()
    assert ans == (None, None)  # return an empty heap

    


pytest.main(["-v", "-s", "test_minMaxHeap.py"])       
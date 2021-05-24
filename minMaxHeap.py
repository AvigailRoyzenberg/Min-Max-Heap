import math
import random

''' The Min-Max Heap is a data structure that combines the uses of a 
max-heap and a min-heap. This means we can achieve retrieval in O(1) time
and insertion/deletion in O(log(n)) time of both the mins and maxes. 
At even levels of the tree - each node is less then all of its children, 
while at odd levels - each node is greater than all of its children '''

class Node(object):
    def __init__(self, k, d):
        self.key  = k
        self.data = d
        
    def __str__(self): 
        return "(" + str(self.key) + "," + repr(self.data) + ")"
    
    def __repr__(self):
        return str(self)
   
   
class minMaxHeap(object):
    def __init__(self, size):
        self.__arr = [None] * size  # reperesented as an array (making it an implicit data structure)
        self.__nElems = 0           # keeps track of how many elements inserted
    
    
    def insert(self, k, d):
        if self.__nElems == len(self.__arr): return False  # fail if the heap is full
        
        self.__arr[self.__nElems] = Node(k, d)    # place new node at end of heap
        self.push_up(self.__nElems)               # trickle it up
        self.__nElems += 1                      
        return True
    
    
    def lenHeap(self):
        return self.__nElems
    
    
    def push_up(self, i):
        if i != 0:  # if the index is not at the root 
            
            # The ith location in the array will correspond to a node located on the level |log i| in the heap.
            level = math.floor(math.log2(i + 1)) 
            parent_index = (i-1) // 2             # the parent's location
            
            if level % 2 == 0:                                                                         # if the index is on a min level
                if self.__arr[i].key > self.__arr[parent_index].key:                                   # if it's bigger than the parent which is on the max level
                    self.__arr[i], self.__arr[parent_index] = self.__arr[parent_index], self.__arr[i]  # swap them
                    self.pushUpMax(parent_index)                                                       # trickle it up
                else:                                                                                  # if it's bigger than the parent
                    self.pushUpMin(i)                                                                  # otherwise we're still on the min level and we push up that index
                    
            else:                                                                                      # if the index is on a max level
                if self.__arr[i].key < self.__arr[parent_index].key:
                    self.__arr[i], self.__arr[parent_index] = self.__arr[parent_index], self.__arr[i]
                    self.pushUpMin(parent_index)
                else:
                    self.pushUpMax(i)
        
                    
    def pushUpMax(self, i):
        # index location of:
        parent = (i-1) // 2 
        grandparent = (parent-1) // 2 
        
        if grandparent >= 0 and self.__arr[i].key > self.__arr[grandparent].key:             # if it's a valid index AND the element that we'r on > than our granparent
            self.__arr[i], self.__arr[grandparent] = self.__arr[grandparent], self.__arr[i]  # swap them
            self.pushUpMax(grandparent)
      
                    
    def pushUpMin(self, i):
        # index location of:
        parent = (i-1) // 2
        grandparent = (parent-1) // 2
        
        if grandparent >= 0 and self.__arr[i].key < self.__arr[grandparent].key:             #if it's a valid index AND the element that we'r on is < than our granparent
            self.__arr[i], self.__arr[grandparent] = self.__arr[grandparent], self.__arr[i]  # swap them
            self.pushUpMin(grandparent)
    
            
    def findMin(self):
        if self.__nElems == 0: return None  # if it's empty, return None
        return self.__arr[0].key            # otherwise, the root node is always the min
    
    
    def findMax(self):
        if self.__nElems == 0: return None  # if it's empty
        
        if self.__nElems < 3:      
            return self.__arr[1].key
        else:
            return max(self.__arr[1].key, self.__arr[2].key)  # the max of the elements on the 1st max level
          
            
    def pushDownMin(self, i):
        if i < self.__nElems // 2:                     # if i'th location has children
            m = self.findSmallestChildIndex(i)
            if m != (2*i)+1 and m != (2*i) +2:         # if it's not equal to any of these then m must be a grandchild index
                if self.__arr[m].key < self.__arr[i].key:
                    self.__arr[m], self.__arr[i] = self.__arr[i], self.__arr[m] # swap them
                    
                    if self.__arr[m].key > self.__arr[(m-1)//2].key:
                        self.__arr[m], self.__arr[(m-1)//2] = self.__arr[(m-1)//2], self.__arr[m] # swap them
                        
                    self.pushDownMin(m)
                    
            elif self.__arr[m].key < self.__arr[i].key: 
                self.__arr[m], self.__arr[i] = self.__arr[i], self.__arr[m] # swap them
      
                
    def pushDownMax(self, i):
        if i < self.__nElems // 2:                     # if the i'th location has children
            m = self.findGreatestChildIndex(i)
            if m != (2*i) +1 and m != (2*i) +2:        # if it's not equal to any of these then m must be a grandchild index
                if self.__arr[m].key > self.__arr[i].key:
                    self.__arr[m], self.__arr[i] = self.__arr[i], self.__arr[m] # swap them
                    
                    if self.__arr[m].key < self.__arr[(m-1)//2].key:
                        self.__arr[m], self.__arr[(m-1)//2] = self.__arr[(m-1)//2], self.__arr[m] # swap them
                        
                    self.pushDownMax(m)
                    
            elif self.__arr[m].key > self.__arr[i].key: 
                self.__arr[m], self.__arr[i] = self.__arr[i], self.__arr[m] # swap them
    
    
    def findSmallestChildIndex(self, i):
        leftChild = (2 *i) + 1                         # left child location
        rightChild = (2 *i) + 2                        # right child location
        lefts_leftGrandchild = (leftChild * 2) + 1     # left child of the grandchild of the left child
        lefts_rightGrandchild = (leftChild * 2) + 2    # right child of grandchild of the left child
        rights_leftGrandchild = (rightChild * 2) + 1   # left child of the grandchild of the right child
        rights_rightGrandchild = (rightChild * 2) + 2  # right child of the grandchild of the right child
        
        minIndex = leftChild                           # we start with the first child we'd assume we'd have
        
        # if the index is in range of our array (if it's a valid index) AND if the element there is smaller
        if rightChild < self.__nElems and self.__arr[rightChild].key < self.__arr[minIndex].key:
            # save it as our minimum index
            minIndex = rightChild    
            
        if lefts_leftGrandchild < self.__nElems and self.__arr[lefts_leftGrandchild].key < self.__arr[minIndex].key:
            minIndex = lefts_leftGrandchild
        
        if lefts_rightGrandchild < self.__nElems and self.__arr[lefts_rightGrandchild].key < self.__arr[minIndex].key:
            minIndex = lefts_rightGrandchild
        
        if rights_leftGrandchild < self.__nElems and self.__arr[rights_leftGrandchild].key < self.__arr[minIndex].key:
            minIndex = rights_leftGrandchild
        
        if rights_rightGrandchild < self.__nElems and self.__arr[rights_rightGrandchild].key < self.__arr[minIndex].key:
            minIndex = rights_rightGrandchild       
        
        
        return minIndex
            

    def findGreatestChildIndex(self, i):
        leftChild = (2 *i) + 1                         # left child location
        rightChild = (2 *i) + 2                        # right child location
        lefts_leftGrandchild = (leftChild * 2) + 1     # left child of the grandchild of the left child
        lefts_rightGrandchild = (leftChild * 2) + 2    # right child of grandchild of the left child
        rights_leftGrandchild = (rightChild * 2) + 1   # left child of the grandchild of the right child
        rights_rightGrandchild = (rightChild * 2) + 2  # right child of the grandchild of the right child
        
        maxIndex = leftChild                           # we start with the first child we'd assume we'd have
        
        # if the index is in range of our array (if it's a valid index) AND if the element there is bigger
        if rightChild < self.__nElems and self.__arr[rightChild].key > self.__arr[maxIndex].key:
            # save it as our minimum index
            maxIndex = rightChild                     
            
        if lefts_leftGrandchild < self.__nElems and self.__arr[lefts_leftGrandchild].key > self.__arr[maxIndex].key:
            maxIndex = lefts_leftGrandchild
        
        if lefts_rightGrandchild < self.__nElems and self.__arr[lefts_rightGrandchild].key > self.__arr[maxIndex].key:
            maxIndex = lefts_rightGrandchild
        
        if rights_leftGrandchild < self.__nElems and self.__arr[rights_leftGrandchild].key > self.__arr[maxIndex].key:
            maxIndex = rights_leftGrandchild
        
        if rights_rightGrandchild < self.__nElems and self.__arr[rights_rightGrandchild].key > self.__arr[maxIndex].key:
            maxIndex = rights_rightGrandchild       
        
        return maxIndex        
            

    def removeMin(self):
        if self.__nElems == 0: return None, None       # empty heap
        
        root = self.__arr[0]
        self.__nElems -= 1
         
        self.__arr[0] = self.__arr[self.__nElems]      # place the last Node in the heap into the root location
        self.pushDownMin(0)                            # and push it down
        
        return root.key, root.data
    
    
    def removeMax(self):
        if self.__nElems == 0: return None, None       # if it's an empty heap
        
        if self.__nElems == 1:                         # if there's 1 element
            self.__nElems -= 1
            return self.__arr[0].key, self.__arr[0].data
        
        if self.__nElems == 2:                         # if there's 2 elements
            self.__nElems -= 1
            return self.__arr[1].key, self.__arr[1].data
        
        if self.__nElems >= 3:                         # if there's 3 or more
            self.__nElems -= 1
            maxIndex = 1                               # arbitrarily choose the 1st index
            if self.__arr[2].key > self.__arr[1].key:  # if the second is bigger
                maxIndex = 2                           # set that to be the max index
                
            maxNode = self.__arr[maxIndex]             # use the index to get the maxNode
            self.__arr[maxIndex] = self.__arr[self.__nElems]
            self.pushDownMax(maxIndex)
            
            return maxNode.key, maxNode.data
        
        
'''
O(NlgN); Unstable; Inplace
'''
def buildMaxHeap(arr):    # O(N)
    n = len(arr)
    for i in range(n//2, -1, -1):
        # do heapify from the first inner node
        heapify(arr, i)

def heapify(arr, i):     # O(lgN)
    left = 2*i + 1
    right = 2*i + 2
    # find the largest node among left/right child and parent node
    largest = i
    if left  < heapSize and arr[left] > arr[largest]:
        largest = left
    if right  < heapSize and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heapSort(arr):
    global heapSize        # define heap size as global variable
    heapSize = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1, 0, -1):
        # put the root(largest value) to the end and do heapify on the new root
        swap(arr, 0, i)
        heapSize -= 1
        heapify(arr, 0)
    return arr

if __name__ == '__main__':
    arr = [10, 4, 2, 11, 8, 9, 5, 13, 14, 12, 7, 6, 15, 1, 3]
    heapSize = len(arr)
    print('After heapSort: ', heapSort(arr))
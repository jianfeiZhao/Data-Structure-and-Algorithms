class MinHeap:
    def __init__(self, ls):
        self.heapSize = len(ls)
        self.arr = self.buildMinHeap(ls)

    def buildMinHeap(self, arr):    # O(N)
        n = len(arr)
        for i in range(n//2, -1, -1):
            # do heapify from the first inner node
            self.heapify(arr, i)
        return arr

    def heapify(self, arr, i):     # O(lgN)
        left = 2*i + 1
        right = 2*i + 2
        # find the smallest node among left/right child and parent node
        smallest = i
        if left  < self.heapSize and arr[left] < arr[smallest]:
            smallest = left
        if right  < self.heapSize and arr[right] < arr[smallest]:
            smallest = right
        if smallest != i:
            self.swap(arr, i, smallest)
            self.heapify(arr, smallest)

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def extractMin(self):
        minn = self.arr[0]
        self.swap(self.arr, 0, self.heapSize-1)
        del self.arr[self.heapSize-1]
        self.heapSize -= 1
        self.heapify(self.arr, 0)
        return minn

    def heapDecreaseKey(self, i, key):
        #print(self.arr)
        if key > self.arr[i]:
            return print('Heap under flow')
        self.arr[i] = key
        while i>0 and self.arr[(i-1)//2] > self.arr[i]:
            self.swap(self.arr, (i-1)//2, i)
            i = (i-1)//2

    def Insert(self, key):
        self.heapSize += 1
        self.arr.append(9999)
        self.heapDecreaseKey(self.heapSize-1, key)
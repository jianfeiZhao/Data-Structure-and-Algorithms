'''
Every time select the smallest value and put it at the start

O(N^2); In place; Unstable;

Used in small amount of data
'''
def selectSort(arr):
    for i in range(len(arr)-1):
        # record the index of min data
        minIndex = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

if __name__ == '__main__':
    arr = [10, 4, 2, 11, 8, 9, 5, 13, 14, 12, 7, 6, 15, 1, 3]
    print('After selectSort: ', selectSort(arr))
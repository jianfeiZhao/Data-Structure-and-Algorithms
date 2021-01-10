'''
Find the maximum sum of subarray
'''
def maxSubarray(arr, low=None, high=None):
    low = 0 if not isinstance(low, (int, float)) else low
    high = len(arr)-1 if not isinstance(high, (int, float)) else high

    if low == high:
        return arr[low]

    mid = (low+high)//2
    
    m1 = maxSubarray(arr, low, mid)     # find max sum in left half
    m2 = maxSubarray(arr, mid+1, high)     # find max sum in right half
    m3 = maxCrossSubarray(arr, low, mid, high)    # find max sum cross the subarray
  
    return max(m1, m2, m3)

def maxCrossSubarray(arr, low, mid, high):
    leftSum = -1
    sum  = 0
    for i in range(mid, low-1, -1):
        sum += arr[i]
        if sum > leftSum:
            leftSum = sum
            maxLeft = i

    rightSum = -1
    sum  = 0
    for j in range(mid+1, high+1):
        sum += arr[j]
        if sum > rightSum:
            rightSum = sum
            maxRight = j

    return leftSum + rightSum 

if __name__ == '__main__':
    arr = [10, -4, 2, 11, -8, 9, -5, 13, -14, 12, -7, -6, 15, -1, 3]
    print('Maximum subarray: ', maxSubarray(arr))

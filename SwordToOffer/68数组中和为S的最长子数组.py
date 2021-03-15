def maxSubSum(arr, S):
    if not arr: return []
    result = []
    seqSum = 0
    seq = []
    for i in arr:
        seq.append(i)
        seqSum += i
        while seqSum > S:
            seqSum -= seq.pop(0)
        if seqSum == S:
            if len(seq) > len(result):
                result = seq
                #print(result)
    return result

arr = [1,1,1,3,2,2]
maxSubSum(arr, 4)
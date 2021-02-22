'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''
import functools

class Solution:
    '''
自定义函数用于排序，对于两个数a,b 如果按ab顺序组成的数 > 按ba顺序组成的数，那么看作a > b；
之后按照冒泡排序的思路将输入数组从小到大排序；最后将排序后的数组连接成数字输出。
    '''
    def printMinNumber(self, numbers):
        if numbers == []:
            return ''
        # define the compare function
        def contrast(a, b):
            s1 =  int(str(a)+str(b))
            s2 =  int(str(b)+str(a))
            if s1 > s2:
                return 1
            elif s1 < s2:
                return -1
            else:
                return 0
        # BubbleSort
        for i in range(len(numbers)-1):
            for j in range(i, len(numbers)):
                if contrast(numbers[i], numbers[j]) == 1:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        # print the result
        s = str()
        for i in range(len(numbers)):
            s += str(numbers[i])
        return int(s)
    
    '''
利用lambda表达式和sort函数，程序会更简洁。
    '''
    def printMinNumber2(self, numbers):
        if not numbers: return ''
        numbers = list(map(str, numbers))
        numbers.sort(key=functools.cmp_to_key(lambda x, y: 1 if x+y>y+x else -1))  # self-define comparison method, sort() ascending order by default
        return int(''.join(x for x in numbers))


ls = [434, 31, 233, 666, 99, 454, 31]
s = Solution()
print(s.printMinNumber(ls))
print(s.printMinNumber2(ls))
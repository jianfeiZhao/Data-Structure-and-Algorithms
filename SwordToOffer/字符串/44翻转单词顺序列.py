'''
“student. a am I” --> “I am a student.”
'''
class Solution:
    def reverseSentence(self, s):
        s = s.split(' ')   
        s.reverse()
        return ' '.join(s)

s = Solution()
sent = 'student. a am I'
print(s.reverseSentence(sent))
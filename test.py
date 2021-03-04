str1 = 'DBACEGF' 
str2 = 'ABCDEFG'

class Vertex:
    def __init__(self, n):
        self.name = n
        self.left = None
        self.right = None
        self.color = 'white'
        self.pred = None    # predecessor(parent)

class Solution:
    def reconstructBinaryTree(self, pre, tin):
        if len(pre) == 0:
            return None
        root = Vertex(pre[0])
        pos = tin.index(pre[0]) ### 根节点在中序遍历中的index，看作左子树的节点个数
        root.left = self.reconstructBinaryTree(pre[1:1+pos], tin[:pos])   # 左子树
        root.right = self.reconstructBinaryTree(pre[pos+1:], tin[pos+1:])   # 右子树
        return root

    def bfs(self, s):
        q = list()
        res = s.name
        s.color = 'gray'
        q.append(s)
        while len(q) > 0:
            u = q.pop(0)
            for v in (u.left, u.right):
                if not v:
                    continue
                if v.color == 'white':
                    res += v.name
                    v.color = 'gray'
                    v.pred = u
                    q.append(v)

                
            u.color = 'black'
        print(res)

s = Solution()
root = s.reconstructBinaryTree(str1, str2)
s.bfs(root)
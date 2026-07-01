class TrieNode:
    def __init__(self):
        self.children={}
        self.word=None
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for w in words:
            node=root
            for c in w:
                if c not in node.children:
                    node.children[c]=TrieNode()
                node=node.children[c]
            node.word=w
        rows,cols=len(board),len(board[0])
        result=[]
        def dfs(r,c,node):
            char=board[r][c]
            if char not in node.children:
                return
            nxt=node.children[char]
            if nxt.word:
                result.append(nxt.word)
                nxt.word=None
            board[r][c]="#"
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, nxt)
            board[r][c] = char
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return result

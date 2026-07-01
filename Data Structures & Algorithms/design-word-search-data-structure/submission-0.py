class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False
class WordDictionary:

    def __init__(self):
        self.data=TrieNode()
        

    def addWord(self, word: str) -> None:
        curr=self.data
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        curr.endOfWord=True
        

    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i==len(word):
                return node.endOfWord
            c=word[i]
            if c=='.':
                for child in node.children.values():
                    if dfs(child,i+1):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                return dfs(node.children[c],i+1)
        return dfs(self.data,0)
            
        

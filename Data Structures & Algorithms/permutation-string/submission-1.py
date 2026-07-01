class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False
        count={}
        for i in s1:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        
        for i in range(len(s2)-(len(s1)-1)):
            j=i
            h={}
            while j<i+len(s1):
                if s2[j] not in h:
                    h[s2[j]]=1
                else:
                    h[s2[j]]+=1
                j+=1
            if count==h:
                return True
                break
        return False

        
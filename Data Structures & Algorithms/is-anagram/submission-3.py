class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        CountS = {}
        CountT = {}

        for n in s:
            CountS[n] = CountS.get(n,0)+1
        
        for l in t:
            CountT[l] = CountT.get(l,0)+1
           

        if CountS == CountT:
            return True 
        
        return False

            

           

        
    

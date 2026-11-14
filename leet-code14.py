class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        self.strs=strs
        a=strs[0]
        ind2=0
        if(len(strs[0])==0):
            return "" 
        alpha=strs[0][0]
        ind=0
        cout=0
        New=""
        for i in strs:
            if (len(i)<=len(a)):
                a=i
            
        for m in range(0,len(a)):
            if(cout>0): break
            alpha=strs[0][m]
            for n in strs:
                if(n[ind]==alpha):
                    None
                else:
                    cout+=1
                    break
            ind+=1
            if(cout==0):
             New=New+alpha
        print(New)
        return New
                    
            
                
            
            
                     
e=Solution()
e.longestCommonPrefix([" "])
                
        
        
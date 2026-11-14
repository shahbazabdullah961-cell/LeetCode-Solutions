class Solution:
    def reverse(self, x: int) -> int:
     self.x=x
     cout=0
     if(x not in range(-2**31,2**31-1)):
         x=0
     if(x<0):
         x=-x
         cout=1
     New=0
     while(int(x)>0):
         temp=int(x%10)
         New=New*10+temp
         x=x/10
     if(cout>0):
         New=-New
     if(New not in range(-2**31,2**31-1)):
         New=0
     print(New)
     return New
e=Solution()
e.reverse(1534236469)
         
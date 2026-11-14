class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
      self.digits=digits
      i=1
      digits[-1]=digits[-1]+1
      while True:
          if(digits[-i]<=9 or len(digits)==1):
              break
          digits[-i]=0
          digits[-(i+1)]=digits[-(i+1)]+1
          
          if(i==len(digits)-1):
              break
          i+=1
      if(digits[0]>9):
          digits[0]=0
          digits.insert(0,1)
      print(digits)
      return digits
     
e=Solution()
e.plusOne([1,1,2,2])
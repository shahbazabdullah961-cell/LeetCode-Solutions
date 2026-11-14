class Solution:
    def addBinary(self, a: str, b: str) -> str:
        self.a=a
        self.b=b
        num1_total=0
        num2_total=0
        arr1=list(a)
        arr2=list(b)
        arr1.reverse()
        arr2.reverse()
        for i in range(0,len(arr1)):
            if(arr1[i]=="1"):
             num1_total+=2**i
        for i in range(0,len(arr2)):
            if(arr2[i]=="1"):
             num2_total+=(2**i)
        result_sum=num1_total+num2_total
        final_str=bin(result_sum)[2:]
        print(final_str)
        return final_str

e=Solution()
e.addBinary("10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101","10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101")
        
        
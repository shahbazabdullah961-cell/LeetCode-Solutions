class Solution:
    def addBinary(self, a: str, b: str) -> str:
        self.a=a
        self.b=b
        num1_total=int(a,2)
        num2_total=int(b,2)
        result_sum=num1_total+num2_total
        return bin(result_sum)[2:]
e=Solution()
e.addBinary("10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101","10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101")
        
        
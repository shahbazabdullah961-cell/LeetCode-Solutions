class Solution:
    def hammingWeight(self, n: int) -> int:
        self.n=n
        bits=n.bit_count()
        return bits


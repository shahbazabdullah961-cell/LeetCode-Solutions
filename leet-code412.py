class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        self.n=n
        fizz=0
        buzz=0
        fizzBuzz=0
        number=1
        array=[]
        while number <= n:
         if(number%3==0 and number%5==0):
          array.append("FizzBuzz")
          fizzBuzz+=1
         elif(number%3==0):
          array.append("Fizz")
          fizz+=1
         elif(number%5==0):
          array.append("Buzz")
          buzz+=1
         else:
          array.append(f"{number}")
         number+=1
        # print(array)
        return array

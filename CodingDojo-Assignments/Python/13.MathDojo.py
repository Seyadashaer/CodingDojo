class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, *nums):
        for num in nums:
            self.result += num
        return self

    def substract(self, *nums):
        for num in nums: 
            self.result -= num
        return self

x = MathDojo()
y = x.add(2).add(9,1,1,1).add(1,2).add(2,6,7,9,10).result
print(y)

m = MathDojo()
r = m.substract(6,5,6,3,2).substract(2,5,6).substract(2,4).result
print(r)

# which is more correct way to solve this assignment?
'''
class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self,num, *nums):
        self.result += num 
        for i in nums:
            self.result += i 
        return self

    def substract(self, num, *nums):
        self.result -= num 
        for i in nums: 
            self.result -= i 
        return self
'''
class Solution:
    def fib(self, n: int) -> int:
        f0 = 0
        f1 = 1
        f2 = f1 + f0
        f3 = f2 + f1

        res1 = f3
        res2 = f2
        res3 = 0


        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return f1 + f0
        elif n == 3:
            return f2 + f1
        else:
            for i in range(4, n+1):
                res3 = res1 + res2
                res2 = res1
                res1 = res3
            return res3
        

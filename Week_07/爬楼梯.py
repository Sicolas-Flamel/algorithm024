# f(n) = f(n-1)+f(n-2)

# 最简
class Solution:
    def climbStairs(self, n: int) -> int:
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a

# 其他解法
class Solution:
    memo = dict()
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        elif n in self.memo:
            return self.memo[n]
        else:
            f = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.memo[n] = f
            return f

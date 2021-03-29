# 判断是否是 2 的幂次方
# 法一：& 运算   n&(-n) = 0
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n > 0) && (n & -n) == n

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and not (n&n-1)
      
# 法二：移位，左移一位，=*2； 右移1位，缩小2倍
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
         return (n>0) && (1<<30) % n == 0;
      
      
      

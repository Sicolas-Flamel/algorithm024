# 也被称为 Hamming Weight。

# built-in function
def hammingWeight(self, n):
    """
    :type n: int
    :rtype: int
    """
    return bin(n).count('1')
  
  # bit operation 
  # n = xxxx1000, n-1= xxxx0111, n&n-1=xxxx0000
  def hammingWeight(self, n):
    """
    :type n: int
    :rtype: int
    """
    c = 0
    while n:
      n &= n-1
      c += 1
    return c

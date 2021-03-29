# https://leetcode.com/problems/reverse-bits/discuss/54740/Python-AC-with-63ms-3lines

def reverseBits(self, n):
        res = 0
        for _ in xrange(32):
            res = (res<<1) + (n&1)
            n>>=1
        return res
      
      
      
      
""" vladn 的答疑非常详细清楚

Let's work on an example. Say, n = 19, which is 00000000000000000000000000010011 in binary, so in the output we should get 11001000000000000000000000000000 in binary, which is 3355443200.
We initialize answer to 0, so in binary it's 32 zeroes. We loop over 32 times, since every integer is gonna have 32 possible 0/1.
1st line in the loop: n & 1, we check if last bit of n is set, is it 1 or 0, ans << 1 we shift all bits that we already have in our answer to the left, so after this shifting the bit on the right is 0, + by using + we set the last bit in the answer to the value that we got in n & 1.
2nd line in the loop we shift bits of our initial number n to the right, since we've already checked the last bit of n, so we just move on to the next bit.

So, in our example, I'm gonna show only first 5 right bits, since other bits are 0.
answer = 0, in binary: 00000000000000000000000000000000
answer << 1 is 00000000000000000000000000000000, n & 1 is 00000000000000000000000000000001
after + operation answer is 00000000000000000000000000000001

answer = 1, in binary: 00000000000000000000000000000001
answer << 1 is 00000000000000000000000000000010, n & 1 is 00000000000000000000000000000001
after + operation answer is 00000000000000000000000000000011

answer = 3, in binary: 00000000000000000000000000000011
answer << 1 is 00000000000000000000000000000110, n & 1 is 00000000000000000000000000000000
after + operation answer is 00000000000000000000000000000110

answer = 6, in binary: 00000000000000000000000000000110
answer << 1 is 00000000000000000000000000001100, n & 1 is 00000000000000000000000000000000
after + operation answer is 00000000000000000000000000001100

answer = 12, in binary: 00000000000000000000000000001100
answer << 1 is 00000000000000000000000000011000, n & 1 is 00000000000000000000000000000001
after + operation answer is 00000000000000000000000000011001

And after that in our example, we'll just shift ** 00000000000000000000000000011001 all the way to the left, which is gonna lead to 11001000000000000000000000000000.

”“”

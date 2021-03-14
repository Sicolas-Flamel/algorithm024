# 斐波那契数列的影子，以及爬楼梯

class Solution:
    def numDecodings(self, s):
        #dp[i] = dp[i-1] 如果 这个字符不等于 0， 那一定可以把这个 i 单独的搞起来
        #       +dp[i-2] 如果 前两个字符刚好可以组合成 [10, 26] 之间的数，那就是 i-1 和 i，两个一起构成一个字符
        if s == "": return 0
        dp = [0 for x in range(len(s)+1)] 给它先初始化了。
        dp[0] = 1
        for i in range(1, len(s)+1):
            if s[i-1] != "0":      #  
                dp[i] += dp[i-1]
            if i != 1 and s[i-2:i] < "27" and s[i-2:i] > "09":  # i!=1 保证这个 i-2 存在
                dp[i] += dp[i-2]
        return dp[len(s)]

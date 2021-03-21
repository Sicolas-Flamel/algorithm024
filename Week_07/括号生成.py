# 体现了剪枝的思路，把 右括号数目<左括号的数目<n/2 变成判别条件，
# 然后就可以优化

# yield 用法
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:  
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p + '(', left-1, right): yield q
                for q in generate(p + ')', left, right-1): yield q
        return list(generate('', n, n))
      

  
# 动态规划大法好      
# 中文链接非常详细   https://www.cxyxiaowu.com/6469.html
# inside 表示一个j对解，afterward 表示一个（i-j-1）对解，我们考虑了它们所有可能的组合
# 1 generate one pair (); 
# 2 generate 0 pair inside, n-1 afterward:(){n-1}个后面的，
#   generate 1 pair inside, n-2 afterward:(())...
#   generate i pair inside, n-i-1 afterward:(())...

class Solution:
     def generateParenthesis(self, n: int) -> List[str]:          
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + inside + ')' + afterward for inside in dp[j] for afterward in dp[i - j - 1]]
        return dp[n]

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
      
      # Python 的解法向来简单粗暴

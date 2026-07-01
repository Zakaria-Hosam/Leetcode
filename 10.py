class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def is_match(i,j):
            if s[i] == p[j] or p[j] == '.':
                return True
        cache = {}
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            #base case
            if j == n:
                return i == m
            #check
            match = (i < m and is_match(i,j)) or (p[j] == '.' and i < m)
            if j+1 < n and p[j+1] == '*':
                #the erase it reality is when * is repeated 0 times, the keep it reality is when * is repeated 1 or more times
                erase_it_reality = dfs(i,j+2)
                keep_it_reality = match and dfs(i+1,j)
                cache[(i, j)] = erase_it_reality or keep_it_reality
                return cache[(i, j)]
            else:
                return match and dfs(i+1,j+1)
        m, n = len(s), len(p)
        i = j = 0
        #edge case no '.' or '*' in pattern
        if '.' not in p and '*' not in p:
            if s == p:
                return True
            elif s != p and '.' not in p and '*' not in p:
                return False
        return dfs(i,j)
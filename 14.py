class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        tcp = ""
        list_of_chars = []
        for j in range(len(strs[0])):
            for i in range(len(strs)):
                if j >= len(strs[i]):
                    return tcp
                list_of_chars.append(strs[i][j])
            if len(set(list_of_chars)) == 1:
                tcp = tcp + strs[i][j]
            else:
                break
            list_of_chars = []
        return tcp
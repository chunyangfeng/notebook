"""
Date: 2023/5/16 14:28

Author: Fengchunyang

Contact: fengchunyang

Record:
    2023/5/16 Create file.

"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min([len(s) for s in strs])
        prefix = ""
        for i in range(min_length):
            tmp = list()
            for j in range(len(strs)):
                tmp.append(strs[j][i])
            if len(list(set(tmp))) == 1:
                prefix += tmp[0]
            else:
                break
            if prefix == "":
                break
        return prefix


if __name__ == '__main__':
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"


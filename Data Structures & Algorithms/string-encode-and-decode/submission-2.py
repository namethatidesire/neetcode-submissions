class Solution:

    def encode(self, strs: List[str]) -> str:
        delim = [[] for i in range(len(strs))]
        for i, s in enumerate(strs):
            delim[i] = f'{len(s)}#'
        res = []
        for i in range(len(strs)):
            res.append(delim[i])
            res.append(strs[i])
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        p = l = r = 0
        print(s)
        while p < len(s):
            print(p)
            l = r = p
            while s[r] != '#':
                r += 1
            sl = int(s[l:r])
            st = s[r+1:r+1 + sl]
            res.append(st)
            p = r+1 + sl
        return res

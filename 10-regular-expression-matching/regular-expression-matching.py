class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        from functools import cache

        @cache
        def f(i, j):
            if j == len(p):
                return i == len(s)

            ok = i < len(s) and p[j] in (s[i], '.')

            if j + 1 < len(p) and p[j + 1] == '*':
                return f(i, j + 2) or (ok and f(i + 1, j))

            return ok and f(i + 1, j + 1)

        return f(0, 0)
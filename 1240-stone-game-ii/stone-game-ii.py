class Solution:
    def stoneGameII(self, p: list[int]) -> int:
        n = len(p)
        s = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            s[i] = s[i + 1] + p[i]

        dp = [[0] * (n + 1) for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                if i + 2 * m >= n:
                    dp[i][m] = s[i]
                else:
                    dp[i][m] = max(
                        s[i] - dp[i + x][max(m, x)]
                        for x in range(1, 2 * m + 1)
                    )

        return dp[0][1]
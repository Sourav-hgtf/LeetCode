class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = [
            "I", "V", "X", "L",
            "C", "D", "M"
        ]

        values = [
            1, 5, 10, 50,
            100, 500, 1000
        ]

        result = 0
        i = 0

        while i < len(s):
            current = symbols.index(s[i])

            if i + 1 < len(s):
                next = symbols.index(s[i + 1])

                if values[current] < values[next]:
                    result += values[next] - values[current]
                    i += 2
                    continue

            result += values[current]
            i += 1

        return result
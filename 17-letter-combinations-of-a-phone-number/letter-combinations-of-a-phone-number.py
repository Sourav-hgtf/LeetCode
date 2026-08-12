class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = [
            "", "", "abc", "def", "ghi", "jkl",
            "mno", "pqrs", "tuv", "wxyz"
        ]

        result = [""]

        for digit in digits:
            new_result = []

            for word in result:
                for char in letters[int(digit)]:
                    new_result.append(word + char)

            result = new_result

        return result
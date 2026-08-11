class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        result = [-1, -1]

        # Find first position
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] >= target:
                if nums[mid] == target:
                    result[0] = mid
                high = mid - 1
            else:
                low = mid + 1

        # Find last position
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] <= target:
                if nums[mid] == target:
                    result[1] = mid
                low = mid + 1
            else:
                high = mid - 1

        return result
        
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        def lcp(left, right):
            min_len = min(len(left), len(right))

            for i in range(min_len):
                if left[i] != right[i]:
                    return left[:i]

            return left[:min_len]

        def divide_and_conquer(left, right):
            if left == right:
                return strs[left]

            mid = (left + right) // 2

            prefix1 = divide_and_conquer(left, mid)
            prefix2 = divide_and_conquer(mid + 1, right)

            return lcp(prefix1, prefix2)

        return divide_and_conquer(0, len(strs) - 1)

strs = ["flower", "flow", "flight"]

solution = Solution()

result = solution.longestCommonPrefix(strs)

print("Longest Common Prefix:", result)
class Solution:
    def longest_substring(self, s: str):
        start = 0
        max_length = 0
        longest_start = 0
        char_index_map = {}

        for end in range(len(s)):
            if s[end] in char_index_map and start <= char_index_map[s[end]]:
                start = char_index_map[s[end]] + 1
            else:
                if end - start + 1 > max_length:
                    max_length = end - start + 1
                    longest_start = start
            char_index_map[s[end]] = end

        return s[longest_start:longest_start + max_length]


string = "aabbcde"
solution = Solution()
result = solution.longest_substring(string)
print(result)

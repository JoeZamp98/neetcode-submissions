class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        all_s_chars = sorted([char for char in s])
        all_t_chars = sorted([char for char in t])

        if all_s_chars == all_t_chars:

            return True

        return False

        
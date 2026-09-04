class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        The cleaned string must be identical whether it is iterated over from the left edge or the right edge.  To test this, we will iterate over from the right and create a list.  Then, iterating from a left, we will test whether the char at each index in this list matches the char at the mirror index in the cleaned string.  If at any point they do not match we return False, otherwise, we can return True.  
        """
        
        cleaned_string = "".join(filter(str.isalnum, s)).lower()

        print(cleaned_string)

        from_r = []

        l = 0
        r = len(cleaned_string) - 1

        while r >= 0:

            from_r.append(cleaned_string[r])

            r -= 1

        while l <= len(cleaned_string) - 1:

            if cleaned_string[l] != from_r[l]:

                return False

            l += 1

        return True


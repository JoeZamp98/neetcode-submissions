class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned_string = "".join(filter(str.isalnum, s)).lower()

        print(cleaned_string)

        from_r = []

        l = 0
        r = len(cleaned_string) - 1

        while r >= 0:

            from_r.append(cleaned_string[r])

            r -= 1

        while l <= len(cleaned_string) - 1:

            if cleaned_string[l] == from_r[l]:

                pass

            else:

                return False

            l += 1

        return True


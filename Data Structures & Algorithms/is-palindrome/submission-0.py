class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned_string = "".join(filter(str.isalnum, s)).lower()

        print(cleaned_string)

        from_r = []
        from_l = []

        l = 0
        r = len(cleaned_string) - 1

        while r >= 0:

            from_r.append(cleaned_string[r])

            r -= 1


        while l <= len(cleaned_string) - 1:

            from_l.append(cleaned_string[l])
            
            l += 1

        if from_r == from_l:
            return True

        return False


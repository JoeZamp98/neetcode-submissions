class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        known_anagrams = {}

        for token in strs:

            sorted_token = str(sorted([x for x in token]))

            if sorted_token not in known_anagrams:

                known_anagrams[sorted_token] = [token]

            elif sorted_token in known_anagrams:

                known_anagrams[sorted_token].append(token)

        grouped_anagrams = [x for x in known_anagrams.values()]

        return grouped_anagrams
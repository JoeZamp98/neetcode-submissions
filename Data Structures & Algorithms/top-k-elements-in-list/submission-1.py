class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_occurences = {}

        for x in nums:
            if x in num_occurences: 
                num_occurences[x] += 1

            else:
                num_occurences[x] = 1

        all_counts = sorted([v for k, v in num_occurences.items()])[::-1]
        top_counts = all_counts[:k]
        top_integers = [k for k, v in num_occurences.items() if v in top_counts]

        return top_integers
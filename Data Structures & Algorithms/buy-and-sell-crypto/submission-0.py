class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buying_price = None
        max_seen_profit = 0
        possible_profit = None

        for idx, p in enumerate(prices):

            if idx == 0:
                buying_price = p
                continue

            else:
                if p < buying_price:
                    buying_price = p
                    
                possible_profit = p - buying_price

                if possible_profit > max_seen_profit:
                    max_seen_profit = possible_profit

            print(f"{max_seen_profit} | {buying_price} | {p} | {possible_profit}")

        return max_seen_profit

            



            


        
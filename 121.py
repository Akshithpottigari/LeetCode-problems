


# Naive Approach:
# Using two for-loops works but as the size increases execution time increases
# It takes almost 15 seconds for an array of length 26000



# def maxProfit(self, prices: List[int]) -> int:
#         max = 0
#         for i in range(len(prices)):
#             for j in range(i+1, len(prices)):
#                 if (prices[j]>prices[i]):
#                     if ((prices[j]-prices[i])>max):
#                         max = prices[j]-prices[i]
#         return max

def maxProfit(prices):
        max = 0
        i=0
        for j in range(len(prices)):
            if (prices[j]>prices[i]):
                if ((prices[j]-prices[i])>max):
                    max = prices[j]-prices[i]
            else:
                i=j
        return max

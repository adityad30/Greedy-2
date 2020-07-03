"""
    T = O(n)
    S = O(n)
    assign 1 candy to all students

    forward pass -> compare ratings[i] > ratings[i-1] and update candies
    backward pass -> compare ratings[i] > ratings[i+1] and update candies
"""
class Solution:
    def candy(self, ratings: List[int]) -> int:
        #edge
        if len(ratings) == 0 or ratings is None:
            return 0

        candies = [1 for i in range(len(ratings))]

        # forward pass
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i -1]  + 1
        print(candies)

        # backward pass
        for j in range(len(ratings) - 2,-1,-1):
            if ratings[j] > ratings[j+1]:
                candies[j] = max(candies[j],candies[j+1]+1)

        print(candies)

        # sum candies
        sum = 0
        for i in range(0,len(candies)):
            sum += candies[i]
        return sum
        

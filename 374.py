class Solution:
    def guessNumber(self, n):

        def binary(low, high):
            mid = (low + high) // 2
            res = guess(mid)

            if res == 0:
                return mid
            elif res == -1:
                return binary(low, mid - 1)
            else:
                return binary(mid + 1, high)

        return binary(1, n)
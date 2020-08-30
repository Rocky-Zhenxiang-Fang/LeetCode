class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrime = [True for _ in range(n)]
        isPrime[0], isPrime[1] = False, False
        end = int(n ** 0.5) + 1
        for i in range(end + 1):
            if not isPrime[i]:
                continue
            j = i * i
            while j < n:
                isPrime[j] = False
                j += i
        count = 0
        for boo in isPrime:
            if boo:
                count += 1
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.countPrimes(10))
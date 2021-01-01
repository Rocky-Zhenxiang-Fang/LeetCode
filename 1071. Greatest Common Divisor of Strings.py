class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        small = str2 if len(str2) <= len(str1) else str1
        big = str1 if small == str2 else str2
        gcd_length = []
        for i in range(len(small), 0, -1):
            if len(small) % i == 0:
                gcd_length.append(i)
        for l in gcd_length:
            small_m = len(small) // l
            big_m = len(big) // l
            sm_2 = small[:l] * small_m
            big_2 = small[:l] * big_m
            if sm_2 == small and big_2 == big:
                return small[:l]
        return ""



if __name__ == '__main__':
    str1 = "ABCABC"
    str2 = "ABC"
    str1_1 = "ABABAB"
    str2_1 = "ABAB"
    sol = Solution()
    print(sol.gcdOfStrings(str1_1, str2_1))




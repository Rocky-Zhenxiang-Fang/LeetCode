class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split(" ")
        res = []
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        for i in range(len(words)):
            sub = []
            word = words[i]
            hold = 0
            for j in range(len(word)):
                if j == 0:
                    if word[j] in vowels:
                        sub.append(word[j])
                        hold = "ma"
                    else:
                        hold = word[j] + "ma"
                else:
                    sub.append(word[j])
            sub.append(hold)
            sub = sub + ["a" * (i + 1)]
            res.append("".join(sub))
        return " ".join(res)


if __name__ == '__main__':
    sol = Solution()
    test_1 = "I speak Goat Latin"
    test_2 = "The quick brown fox jumped over the lazy dog"
    result_1 = "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
    result_2 = "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
    print(sol.toGoatLatin(test_1) == result_1)
    print(sol.toGoatLatin(test_2) == result_2)




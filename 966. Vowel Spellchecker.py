from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        res = []
        words = set(wordlist)
        case_table = {}
        vowel_table = {}
        vowels = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
        for i in range(len(wordlist) - 1, -1, -1):
            w = wordlist[i]
            case_table[w.lower()] = w
            temp = []
            for j in range(len(w)):
                if w[j] in vowels:
                    temp.append("#")
                else:
                    temp.append(w[j].lower())
            vowel_table["".join(temp)] = w

        for q in queries:
            if q in words:
                res.append(q)
                continue
            elif q.lower() in case_table:
                res.append(case_table[q.lower()])
                continue
            temp = []
            for ch in q:
                if ch in vowels:
                    temp.append("#")
                else:
                    temp.append(ch.lower())
            temp = "".join(temp)
            if temp in vowel_table:
                res.append(vowel_table[temp])
                continue
            res.append("")

        return res


if __name__ == '__main__':
    sol = Solution()
    wordlist = ["KiTe", "kite", "hare", "Hare"]
    queries = ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear",
               "keti", "keet", "keto"]

    print(sol.spellchecker(wordlist, queries))
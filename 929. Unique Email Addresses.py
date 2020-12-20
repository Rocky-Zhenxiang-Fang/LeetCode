from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for e in emails:
            e_list = e.split("@")
            local, domain = e_list[0], e_list[1]
            new_local = []
            for c in local:
                if c == ".":
                    continue
                if c == "+":
                    break
                else:
                    new_local.append(c)
            result.add("".join("".join(new_local) + "@" + domain))
        return len(result)


if __name__ == '__main__':
    test1 = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    sol = Solution()
    print(sol.numUniqueEmails(test1))
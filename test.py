# This file is used to review done questions

# Definition for a binary tree node.
from typing import List, Set

import DS


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for e in emails:
            local, domain = e.split("@")
            new_local = []
            for l in local:
                if l == ".":
                    continue
                elif l == "+":
                    break
                else:
                    new_local.append(l)
            result.add("".join(new_local) + "@" + domain)
        return len(result)


if __name__ == '__main__':
    test = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    sol = Solution()
    print(sol.numUniqueEmails(test))

class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        element_stack = []
        temp = []
        for ch in s:
            if ch == "[":
                element_stack.append(temp[:])
                if len(element_stack) > len(count_stack):
                    count_stack.append(1)
                temp = []
            elif ch == "]":
                count = count_stack.pop()
                element_stack[-1].extend(temp * count)
                temp = []
            elif ch.isnumeric():
                count_stack.append(int(ch))
            else:
                temp.append(ch)
        return "".join(element_stack)


if __name__ == "__main__":
    sol = Solution()
    input_string = "3[a]2[bc]"
    print(sol.decodeString(input_string))

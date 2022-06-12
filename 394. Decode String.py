class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        element_stack = []
        curr = []
        dig = 0
        for ch in s: 
            if ch.isdigit():
                dig = dig * 10 + int(ch)              
            elif ch == "[":
                count_stack.append(dig)
                dig =0
                element_stack.append("".join(curr))
                curr = []
            elif ch == "]":
                count = count_stack.pop()
                curr_str = "".join(curr)
                new_curr = [element_stack.pop()] if element_stack else []
                new_curr.append(curr_str * count)
                curr = new_curr
            else:
                curr.append(ch)
        return "".join(element_stack + curr)


if __name__ == "__main__":
    sol = Solution()
    input_strings = ["3[a]2[bc]", '3[a2[c]]', '2[abc]3[cd]ef', "100[leetcode]", "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"]
    for string in input_strings:
        print(sol.decodeString(string))

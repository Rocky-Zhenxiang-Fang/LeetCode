class Solution:
    def isNumber(self, s: str) -> bool:
        """
        Idea:
            Draw the way that the string can involve, and turn it into a state machine
        """
        states = [
            # [0], init state, can go to either a sign or a digit
            {"sign": 1, "digit": 2, "dot": 3},
            # [1], sign state from init, can go to either a dot or a number
            {"dot": 3, "digit": 2},
            # [2], first digit, can go to a dot, "E", itself or the end
            {"dot": 4, "E": 5, "digit": 2, "end": 9},
            # [3], dot state without leading numbers, can only go to another digit
            {"digit": 6},
            # [4], dot state with leading numbers, can go to second number, "E" or the end
            {"digit": 6, "E": 5, "end": 9},
            # [5], E state, can lead to a sign or number
            {"sign": 7, "digit": 8},
            # [6], numbers leading by dot, can go to end, itself or E
            {"end": 9, "digit": 6, "E": 5},
            # [7], sign after E, can only go to a number
            {"digit": 8},
            # [8], digit after E, can go to itself or end
            {"digit": 8, "end": 9}
        ]
        curr_state = 0
        for c in s:
            if c.isdigit():
                curr_state_name = "digit"
            elif c == ".":
                curr_state_name = "dot"
            elif c == "E" or c == "e":
                curr_state_name = "E"
            elif c == "+" or c == "-":
                curr_state_name = "sign"
            elif c == "\n" or c == "\t":
                curr_state_name = "end"
            else:
                return False
            if curr_state_name not in states[curr_state]:
                return False
            else:
                curr_state = states[curr_state][curr_state_name]
        if curr_state not in {2, 4, 6, 8, 9}:
            return False
        else:
            return True


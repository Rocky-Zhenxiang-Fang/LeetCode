class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1_list = list(s1)
        s2_list = list(s2)
        s1_list.sort()
        s2_list.sort()
        return self._break(s1_list, s2_list) or self._break(s2_list, s1_list)
        
    def _break(self, s1, s2):
        for i in range(len(s1)):
            if s2[i] > s1[i]:
                return False
        return True



# TODO: Try it again
        
        
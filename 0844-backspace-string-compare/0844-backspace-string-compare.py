class Solution:
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []

        for el in s:
            if el != "#":
                s_stack.append(el)
            else:
                if len(s_stack) != 0:
                    s_stack.pop()

        for el in t:
            if el != "#":
                t_stack.append(el)
            else:
                if len(t_stack) != 0:
                    t_stack.pop()
        
        # print(s_stack, t_stack)
        return "".join(s_stack) == "".join(t_stack)
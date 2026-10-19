class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "{" or char == "(" or char == "[":
                stack.append(char)
            elif char == "}" or char == ")" or char == "]":
                if stack:
                    if char=="}" and stack[len(stack)-1]=="{":
                        stack.pop()
                    elif char==")" and stack[len(stack)-1]=="(":
                        stack.pop()
                    elif char=="]" and stack[len(stack)-1]=="[":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if not stack:
            return True
        else: 
            return False            

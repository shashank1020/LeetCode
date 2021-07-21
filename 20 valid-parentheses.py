# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        stack = []
        for i in s:
            if i in '({[':
                stack.append(i)
            elif i in ')}]' and stack == []:
                    return False
            else:
                if i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        if stack == []:
            return True
        return False

if __name__ == "__main__":
    a = Solution()
    st = "([}}])"

    print(a.isValid(st))
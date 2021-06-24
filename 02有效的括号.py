# 判断有效的括号

def isValid(s):
    if len(s) % 2 != 0:
        return False

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    stack = list()
    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)

    return not stack


s = "()[]{}"
print(isValid(s))

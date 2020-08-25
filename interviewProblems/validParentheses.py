
def isValid(s):
    """
    checks if parentheses close is valid
    :param s: str
    :return: bool
    """

    stack = []

    parentheses ={"(":")", "[":"]", "{":"}"}

    for char in s:
        if char in parentheses:
            stack.append(char)
        elif not stack or parentheses[stack.pop()] != char:
            return False
    return not stack

if __name__ == "__main__":
    text = "([)}"
    print(isValid(text))
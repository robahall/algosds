def reverseStringTwoPointer(s):
    i, j = 0, len(s)-1
    while (i<j):
        swap(s, i, j)
        i += 1
        j -= 1
    return s

def swap(s, i, j):
    temp = s[i]
    s[i] = s[j]
    s[j] = temp


def reverseString(s):
    """
    Reverse a list recursively
    :param s: (list)
    :return:
    """
    def helper(start, end, ls):
        if start >= end:
            return

        # swap the first and last element
        ls[start], ls[end] = ls[end], ls[start]

        return helper(start + 1, end - 1, ls)

    helper(0, len(s) - 1, s)
    return s





if __name__ == "__main__":
    s = "hello"
    s = [x for x in s]

    print(reverseString(s))
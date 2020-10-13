def isAnagram(s: str, t: str) -> bool:
    """
    Using hash table without Counter and works with unicode.
    """
    if not len(s) == len(t):
        return False
    s_dict = {}
    t_dict = {}
    for idx in range(len(s)):
        if ord(s[idx]) in s_dict:
            s_dict[ord(s[idx])] += 1
        else:
            s_dict[ord(s[idx])] = 1
        if ord(t[idx]) in t_dict:
            t_dict[ord(t[idx])] += 1
        else:
            t_dict[ord(t[idx])] = 1
    if s_dict == t_dict:
        return True
    else:
        return False

if __name__ == "__main__":
    s = 'sudoku'
    t = 'dokusu'
    print(isAnagram(s, t))

import collections

def firstUniqChar(s):
    # Brute Force - O(nlogn)
    len_str = len(s)
    if len_str < 1:
        return - 1

    min_idx = -1
    for idx in range(len_str):
        jdx = 0
        while jdx < len_str:
            if idx != jdx and s[idx] != s[jdx]:
                if jdx == len_str -1:
                    return idx
                else:
                    jdx +=1
            else:
                jdx +=1
    return -1

def firstUniqCharHash(s):
    # Hash Table
    # O(n**2)
    count = collections.Counter(s)

    for idx, char in enumerate(s):
        if count[char] == 1:
            return idx
    return -1





if __name__ == "__main__":
    s = "leetcode"
    print(firstUniqChar(s))
    s1 = "loveleetcode"
    print(firstUniqChar(s1))
    s2 = "eeeettttoooopppppi"
    print(firstUniqChar(s2))
    s3 = "cc"
    print(firstUniqChar(s3))

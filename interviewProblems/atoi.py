import re

def myAtoi(s):
    # Max O(N) using RegEx
    digit = re.compile(r"(-\d+)|[\d+]")
    s = s.strip(" +")
    nums = digit.match(s)
    int_32 = 2**31
    if nums:
        if int_32 * -1 <= int(nums.group(0)) < int_32:
            return int(nums.group(0))
        elif int(nums.group(0)) > int_32:
            return int_32
        else:
            return int_32 * -1
    else:
        return 0

if __name__ == "__main__":
    strs = ["","           -42                ", "+4193 with words", "words and -987", "-91283472332", "+-12"]
    for string in strs:
        my_int = myAtoi(string)
        print(my_int, type(my_int))



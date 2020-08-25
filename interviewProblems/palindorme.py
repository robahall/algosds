
def isPalindrome(s: str) -> bool:
    s = ''.join(x.lower() for x in s if x.isalnum())
    return True if s[:] == s[::-1] else False

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))
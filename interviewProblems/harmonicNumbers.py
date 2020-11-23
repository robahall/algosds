def harmonicNum(n):
    if n == 1:
        return 1
    else:
        return harmonicNum(n-1) + 1/(n-1)


if __name__ == "__main__":
    print(harmonicNum(4))

def fizzBuzz(n):
    out = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(i)
    return out


if __name__ == "__main__":
    print(fizzBuzz(15))
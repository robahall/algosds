import re

def evaluateRPN(tokens):
    queue = []
    regex = re.compile(r"-?\d")
    for value in tokens:
        if regex.match(value):
            queue.append(value)
        else:
            first = queue.pop()
            queue.append(str(int(eval(queue.pop() + value + first))))
    return queue[0]

if __name__ == "__main__":
    arr = ["2", "1", "+", "3", "*"]
    print(evaluateRPN(arr))

    arr2 = ["4", "13", "5", "/", "+"]
    print(evaluateRPN(arr2))

    arr3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(evaluateRPN(arr3))

    arr4 = ["3","11","+","5","-"]
    print(evaluateRPN(arr4))

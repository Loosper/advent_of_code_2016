numberpad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


class MyNumber():
    def __init__(self, value):
        self.value = value

    def increment(self, offset):
        self.value += offset
        if self.value > 2:
            self.value = 2
        if self.value < 0:
            self.value = 0

height = MyNumber(1)
width = MyNumber(1)
code = ''
mapping = {
    'U': lambda: height.increment(-1),
    'D': lambda: height.increment(1),
    'L': lambda: width.increment(-1),
    'R': lambda: width.increment(1)
}

while True:
    try:
        instructions = input()
    except EOFError:
        break

    for instruction in instructions:
        mapping[instruction]()
    code += str(numberpad[height.value][width.value])

print(code)

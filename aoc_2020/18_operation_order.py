#!/usr/bin/env python3

def solve_exp(exp, visited, idx):
    total = 0
    _buffer = []
    op = None
    for i, c in enumerate(exp):
        if not visited[i + idx]:
            visited[i + idx] = 1

            if c == "+" or c == "*":
                op = c
            elif c == "(":
                _buffer.append(solve_exp(exp[i + 1:], visited, i + 1 + idx))
            elif c == ")":
                if _buffer:
                    return _buffer[0]
            else:
                _buffer.append(int(c))

            if len(_buffer) == 2:
                total = _buffer[0] * _buffer[1] if op == "*" else _buffer[0] + _buffer[1]
                _buffer = [total]

    return _buffer[0]

def pop_from_stack(_stack, precedence, _postfix):
    while _stack and _stack[-1] in precedence.keys():
        _postfix.append(_stack.pop())

def solve_postfix(_postfix):
    _stack = []
    op = None

    for i, c in enumerate(_postfix):
        if c == "*":
            _stack.append(_stack.pop() * _stack.pop())
        elif c == "+":
            _stack.append(_stack.pop() + _stack.pop())
        else:
            _stack.append(int(c))

    return _stack[-1]

def part_1(data_list):
    _sum = 0
    for eq in data_list:
        visited = [0 for i in range(len(eq))]
        _sum += solve_exp(eq, visited, 0)

    return _sum

def part_2(data_list):
    precedence = {"*": 0, "+": 1}
    _sum = 0
    for exp in data_list:
        _stack = []
        _postfix = []
        for i, c in enumerate(exp):
            if c == "(":
                _stack.append(c)
            elif c == ")":
                pop_from_stack(_stack, precedence, _postfix)
                _stack.pop()
            elif c in precedence.keys():
                if not _stack or _stack[-1] not in precedence.keys():
                    _stack.append(c)
                elif precedence[_stack[-1]] <= precedence[c]:
                    _stack.append(c)
                else:
                    pop_from_stack(_stack, precedence, _postfix)
                    _stack.append(c)
            else:
                _postfix.append(c)

        pop_from_stack(_stack, precedence, _postfix)
        _sum += solve_postfix(_postfix)

    return _sum

if __name__ == "__main__":
    with open("18.txt", "r") as f:
        data = f.read()

    data_list = data.strip().replace(" ", '').split("\n")

    print("Sum: {}".format(part_1(data_list)))
    print("Sum with precedence: {}".format(part_2(data_list)))

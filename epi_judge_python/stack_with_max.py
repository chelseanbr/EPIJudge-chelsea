from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    def __init__(self):
        self.items = []
        self.max_vals = []

    def empty(self) -> bool:
        return len(self.items) == 0

    def max(self) -> int:
        if self.empty():
            return None
        return self.max_vals[-1]

    def pop(self) -> int:
        if self.empty():
            return None
        item = self.items.pop()
        if self.max_vals[-1] == item:
            self.max_vals.pop()
        return item

    def push(self, x: int) -> None:
        self.items.append(x)
        if len(self.max_vals) == 0 or x >= self.max_vals[-1]:
            self.max_vals.append(x)


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))

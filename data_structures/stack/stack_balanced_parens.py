# YouTube Video: https://www.youtube.com/watch?v=TC7apM-xGaU
"""
Use a stack to check whether or not a string
has balanced usage of parenthesis.
"""

from stack import Stack


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        # if the element at the position index is an opening paren,
        # push it to the stack
        print(f'Index: {index}, paren: {paren}')
        if paren in "([{":
            s.push(paren)
            print(f'Stack: {s.get_stack()}')
        else:
            print('Not an opening paren')
            # if the next element is empty, parens are not balanced
            if s.is_empty():
                is_balanced = False
            else:
                # if next element is not empty or an opening paren,
                # pop the top element off the stack, and
                # compare it to the expected closing paren
                top = s.pop()
                print(f'Stack: {s.get_stack()}')
                if not is_match(top, paren):
                    is_balanced = False

            print(f'popped: {top}, paren: {paren}, balanced: {is_balanced}')

        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False


# test
test_s = ["(((({}))))",
          "[][]]]",
          "[][]"]

for s in test_s:
    print(s)
    is_paren_balanced(s)
    print()

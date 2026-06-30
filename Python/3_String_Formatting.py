# https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true


def print_formatted(number):
    width = len(f"{number:b}")

    # ">" is used to right-align the output within the specified width
    for i in range(1, number + 1):
        print(f"{i:>{width}d} {i:>{width}o} {i:>{width}X} {i:>{width}b}")

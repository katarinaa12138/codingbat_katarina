def lone_sum(a, b, c):
    """
    Given three integer values a, b, and c, return their sum. However, if one of the values is the same as another value,
    it does not count towards the sum.

    Args:
    - a: an integer value
    - b: an integer value
    - c: an integer value

    Returns:
    - The sum of a, b, and c, excluding any values that appear more than once.
    """
    l = [a, b, c]
    result = 0
    for x in l:
        if l.count(x) == 1:
            result += x
    return result


# print(lone_sum(1, 2, 3))
# print(lone_sum(3, 2, 3))
# print(lone_sum(3, 3, 3))


def main():
    test_cases = [(1, 2, 3), (3, 2, 3), (3, 3, 3)]

    for a, b, c in test_cases:
        result = lone_sum(a, b, c)
        print(f"Input: a={a}, b={b}, c={c}, Output: {result}")


if __name__ == "__main__":
    main()

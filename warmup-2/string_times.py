def string_times(str, n):
    """
    Given a string `str` and a non-negative integer `n`, return a larger string that consists of `n` copies of the original string.

    Args:
    - str: a string
    - n: a non-negative integer

    Returns:
    - A string consisting of `n` copies of the original string `str`
    """
    return str * n


# Main function
def main():
    test_cases = [("Hi", 2), ("Hi", 3), ("Hi", 1)]

    for str, n in test_cases:
        result = string_times(str, n)
        print(f"String: '{str}', n: {n}, Result: '{result}'")


if __name__ == "__main__":
    main()

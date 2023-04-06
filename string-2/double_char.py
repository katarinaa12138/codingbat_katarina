def double_char(string):
    """
    Given a string `string`, return a string where for every character in the original string, there are two characters.

    Args:
    - string: a string to be doubled

    Returns:
    - A string where each character in the original string appears twice.
    """
    new_string = ""
    for char in string:
        new_string += char * 2
    return new_string


# Main function
def main():
    test_cases = ["The", "AAbb", "Hi, there"]

    for string in test_cases:
        result = double_char(string)
        print(f"Input: {string}, Output: {result}")


if __name__ == "__main__":
    main()

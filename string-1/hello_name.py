def hello_name(name):
    """
    Given a string `name`, return a greeting of the form "Hello `name`!".

    Args:
    - name: a string representing the name of a person.

    Returns:
    - A string that greets the person with their name, in the format "Hello `name`!".
    """
    return f"Hello, {name}!"
    # return "Hello " + name + "!"


# Main Function
def main():
    test_cases = ["Bob", "Alice", "X"]

    for name in test_cases:
        result = hello_name(name)
        print(f"Input: {name}, Output: {result}")


if __name__ == "__main__":
    main()

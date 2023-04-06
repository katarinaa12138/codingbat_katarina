def sleep_in(weekday, vacation):
    """
    Given two boolean inputs `weekday` and `vacation`, where `weekday` is True if it is a weekday and False otherwise,
    and `vacation` is True if we are on vacation and False otherwise,
    return True if we sleep in (i.e., it is not a weekday or we're on vacation).

    Args:
    - weekday: a boolean value indicating whether or not it is a weekday
    - vacation: a boolean value indicating whether or not we are on vacation

    Returns:
    - A boolean value indicating whether or not we sleep in
    """
    if not weekday or vacation:
        return True
    else:
        return False

    # return not weekday or vacation


# Main function
def main():
    test_cases = [(False, False), (True, False), (False, True)]

    for weekday, vacation in test_cases:
        result = sleep_in(weekday, vacation)
        print(f"Weekday: {weekday}, Vacation: {vacation}, Sleep in? {result}")


if __name__ == "__main__":
    main()

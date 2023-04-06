def cigar_party(cigars, is_weekend):
    """
    Determine whether a squirrel party with the given number of cigars and whether it is the weekend is successful.

    A squirrel party is successful when the number of cigars is between 40 and 60, inclusive.
    However, if it is the weekend, then there is no upper bound on the number of cigars.

    Args:
    - cigars: an integer representing the number of cigars at the party
    - is_weekend: a boolean indicating whether or not it is the weekend

    Returns:
    - True if the party is successful (i.e. the number of cigars is between 40 and 60 inclusive, or there is no upper bound on the number of cigars because it is the weekend), False otherwise.
    """
    if is_weekend:
        if cigars >= 40:
            return True
        else:
            return False
    else:
        if 40 <= cigars <= 60:
            return True
        else:
            return False

    # return is_weekend or (not is_weekend and 40 <= cigars <= 60)


# print(cigar_party(30, False))
# print(cigar_party(40, False))
# print(cigar_party(50, False))
# print(cigar_party(70, True))


# Main function
def main():
    test_cases = [(30, False), (50, False), (70, True), (40, False)]

    for cigars, is_weekend in test_cases:
        result = cigar_party(cigars, is_weekend)
        print(f"Cigars: {cigars}, Weekend: {is_weekend}, Success: {result}")


if __name__ == "__main__":
    main()

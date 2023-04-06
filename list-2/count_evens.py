def count_evens(nums):
    """
    Return the number of even integers in the given list.

    Args:
    - nums: a list of integers

    Returns:
    - The number of even integers in the input list
    """
    even = 0
    for i in nums:
        if i % 2 == 0:
            even += 1
    return even 
    # evens = 0
    # for number in nums:
    #     if number % 2 == 0:
    #         evens += 1
    # return evens


# TEST
# print(count_evens([2, 1, 2, 3, 4]))
# print(count_evens([2, 2, 0]))
# print(count_evens([1, 3, 5]))


# Main function
def main():
    test_cases = [[2, 1, 2, 3, 4], [2, 2, 0], [1, 3, 5]]

    for nums in test_cases:
        print(f"{nums}: {count_evens(nums)}")


if __name__ == "__main__":
    main()

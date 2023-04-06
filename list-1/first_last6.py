def first_last6(nums):
    """
    Given an array of ints, return True if 6 appears as either the first or last element in the array.
    The array will be length 1 or more.

    Args:
    - nums: a list of integers

    Returns:
    - True if the first or last element of nums is 6, False otherwise
    """
    if nums[0] == 6 or nums[-1] == 6:
        return True
    else:
        return False
    # return nums[0] == 6 or nums[-1] == 6

# TEST
# print(first_last6([1, 2, 6]))
# print(first_last6([6, 1, 2, 3]))
# print(first_last6([13, 6, 1, 2, 3]))

# Main function
def main():
    test_cases = [
        [1, 2, 6],
        [6, 1, 2, 3],
        [13, 6, 1, 2, 3]
    ]
    
    for nums in test_cases:
        print(f"{nums}: {first_last6(nums)}")
        
if __name__ == '__main__':
    main()

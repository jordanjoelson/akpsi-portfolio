def sum3(nums):
    if len(nums) == 3:
        return sum(nums)
    else:
        raise ValueError("Input list must contain exactly three integers.")

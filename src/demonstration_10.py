"""
Challenge #10:

Create a function that applies a discount d to every number in the list.

Examples:
- get_discounts([2, 4, 6, 11], "50%") ➞ [1, 2, 3, 5.5]
- get_discounts([10, 20, 40, 80], "75%") ➞ [7.5, 15, 30, 60]
- get_discounts([100], "45%") ➞ [45]

Notes:
- The discount is the percentage of the original price (i.e the discount of
"75%" to 12 would be 9 as opposed to taking off 75% (making 3)).
- There won't be any awkward decimal numbers, only 0.5 to deal with.
"""

# PASS BY COPY - preserve original values
# def get_discounts(nums, percentage):
#     discount_percent = int(percentage[ : -1]) / 100
#     new_nums = []
#     for num in nums:
#         # apply the discount
#         new_nums.append( num * discount_percent)
#     return new_nums

# PASS BY REFERENCE - does not preserve 
# original values, will be directly modified
def get_discounts(nums, percentage):
    discount_percent = int(percentage[ : -1]) / 100
    for i in range(0, len(nums)):
        # apply the discount
        nums[i] = nums[i] * discount_percent
    return nums

original_nums = [10, 20, 40, 80]

print(get_discounts(original_nums, "75%"))

print(original_nums)


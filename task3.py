# pointing the list
def find_indices_to_add_up(numbers, target):
    left, right = 0, len(numbers) - 1 

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return left, right
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None  # If no such numbers are found

# Example of non-decreasing list
numbers_list = [1, 3, 5, 7, 9, 11, 13, 15]
target_sum = 10

result = find_indices_to_add_up(numbers_list, target_sum)

if result is not None:
    index1, index2 = result
    print(f"Indices with values {numbers_list[index1]} and {numbers_list[index2]} add up to the target sum.")
else:
    print("No such numbers found in the list.")

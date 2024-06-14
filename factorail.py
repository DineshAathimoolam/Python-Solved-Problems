def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Test the function
numbers = [10, 5, 8, 20, 3]
largest_num = find_largest(numbers)
print(f"The largest number is {largest_num}")

def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def calculate_average(numbers):
    sum_of_numbers = calculate_sum(numbers)
    average = sum_of_numbers // len(numbers)
    return average

# A list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate and print the average of the numbers
print(f"The average is: {calculate_average(numbers)}")

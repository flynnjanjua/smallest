Implement a program to find the largest and smallest numbers in a given list:
python
Copy code
def find_largest_smallest(numbers):
    if len(numbers) == 0:
        return None, None
    smallest = largest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return smallest, largest

input_list = input("Enter a list of numbers separated by spaces: ")
numbers = [int(num) for num in input_list.split()]

smallest_num, largest_num = find_largest_smallest(numbers)

if smallest_num is None:
    print("No numbers were entered.")
else:
    print("Smallest number:", smallest_num)
    print("Largest number:", largest_num)

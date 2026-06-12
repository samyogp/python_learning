# finding largest number from the list
numbers = [45, 12, 89, 34, 67]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
        print(f"Largest: {largest}")
        
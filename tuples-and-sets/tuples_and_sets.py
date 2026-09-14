# Tuples: fixed, ordered data that shouldn't change
# Good for things like coordinates or fixed records

point = (4, 7)
print(f"Point: {point}")
print(f"X: {point[0]}, Y: {point[1]}")

# Sets: unordered collections of unique values
# Good for removing duplicates or checking membership fast

numbers = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = set(numbers)
print(f"\nOriginal list: {numbers}")
print(f"Unique values: {unique_numbers}")

# Practical exercise: dedupe a list of numbers entered by the user

print("\nEnter numbers one at a time. Type 'done' when finished.")
user_numbers = []

while True:
    entry = input("Enter a number: ")
    if entry.lower() == "done":
        break
    user_numbers.append(int(entry))

unique_entries = set(user_numbers)
print(f"\nYou entered: {user_numbers}")
print(f"Unique numbers: {unique_entries}")
print(f"You entered {len(user_numbers)} numbers, but only {len(unique_entries)} were unique")
# Task 1 : Build a Calculator CLI App 
import math
def add(nums):
    return sum(nums)
def subtract(nums):
    result = nums[0]
    for n in nums[1:]:
        result -= n
    return result

def multiply(nums):
    result = 1
    for n in nums:
        result *= n
    return result

def divide(nums):
    result = nums[0]
    for n in nums[1:]:
        if n == 0:
            return "Error: Division by zero!"
        result /= n
    return result

def square(n):
    return n * n

def square_root(n):
    if n < 0:
        return "Error: Cannot take square root of negative number!"
    return math.sqrt(n)

print("=== Simple Calculator CLI App ===")

while True:
    print("\nChoose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Square Root")
    print("7. Exit")

    choice = input("Enter choice (1-7): ")

    if choice == '7':
        print("Exiting calculator... Goodbye!")
        break

    if choice not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid choice! Try again.")
        continue

    if choice in ['5', '6']:
        num = float(input("Enter number: "))
        if choice == '5':
            print("Result:", square(num))
        else:
            print("Result:", square_root(num))
        continue

    count = int(input("How many numbers do you want to use? "))

    nums = []
    for i in range(count):
        n = float(input(f"Enter number {i+1}: "))
        nums.append(n)

    if choice == '1':
        print("Result:", add(nums))
    elif choice == '2':
        print("Result:", subtract(nums))
    elif choice == '3':
        print("Result:", multiply(nums))
    elif choice == '4':
        print("Result:", divide(nums))

# it works nice

from time import sleep

# This code defines a generator function called `generate_numbers` that yields three numbers: 1, 2, and 3. When the generator is called, it returns a generator object. 
# The code then uses the `next()` function to retrieve the next value from the generator, with a 1-second pause between each retrieval using `sleep()`.
# def generate_numbers():
#     yield 1
#     yield 2
#     yield 3

# numbers = generate_numbers()
# print(numbers)  # This will print the generator object
# sleep(1)  # Sleep for 1 second before getting the next number
# print(next(numbers))  # This will print 1
# sleep(1)  # Sleep for 1 second before getting the next number
# print(next(numbers))  # This will print 2
# sleep(1)  # Sleep for 1 second before getting the next number
# print(next(numbers))  # This will print 3

# The following code defines a generator function called `generate_numbers` that yields numbers from 1 to 5. 
# It uses a for loop to iterate through the range of numbers, and before yielding each number, it sleeps for 1 second. 
# The generator is then used in a for loop to print each number with a 1-second pause between each print.
def generate_numbers():
    for i in range(1, 6):
        sleep(1)  # Sleep for 1 second before yielding the next number
        yield i

numbers = generate_numbers()

for number in numbers:
    print(number)  # This will print numbers from 1 to 5 with a 1-second pause between each
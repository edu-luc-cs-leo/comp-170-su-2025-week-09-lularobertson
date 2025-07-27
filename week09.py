def factorial(n):
    """Computes recursively n! = 1 * 2 * ... * (n-1) * n
    if n == 0:
        # Base case, 0! is by definition 1
        result = 1
    else:
        # Recursive case: n! = (n-1)! * n
        result = n * factorial(n-1)
    return result
    """
    result = 1
    if n == 0:
        result += 0
    else:
        for i in range(2, n + 1): # i starts at 0 so we need to increase n by one.
            result *= i
    return result

print(factorial(6))

def fibonacci(n):
    """Computes recursively the Fibonacci sequence
    F(n) = F(n-1) + F(n-2)
    for n > 2, with initial conditions F(1) = 1 and F(2) = 2
    if n == 1 or n == 2:
        # Base case
        result = n
    else:
        # Recursive case
        result = fibonacci(n-1) + fibonacci(n-2)
    return result
"""
    if n > 0:
        result = 0
        if n == 1 or n == 2:
            result = n
        else:
            a = 1 # F(1)
            b = 2 # F(2)
            for i in range(3, n + 1):
                temp = a + b #temporary previous number F(3)
                a = b # a is now increased to b
                b = temp # b is increased to temp F(3)
                result = b # finding F(n)
    else:
        result = 0
    return result

print(fibonacci(4))



# ITERATIVE VERSIONS OF ASSIGNMENT METHODS

def sum_of_digits_iterative(n):
    sum = 0
    while n > 1:
        # Obtain the last digit to add to sum. The last digit is always the remainder of
        # the integer division by base of the number system in use (here: 10).
        sum += n % 10 
        # Remove the last digit. This can be done by integer division of the number with
        # its number base (here: 10). For exampe 24 // 10 = 2 (and thus 4 is gone!)
        n //= 10
    # Done
    return sum + n

 

def count_occurrences_iterative(data_list, target):
    count = 0
    # Iterate over the input list
    for i in range(len(data_list)):
        # Check if current list item matches target value
        if data_list[i] == target:
            # If it does, increment the counter
            count += 1
    # Done
    return count


# WRITE YOUR CODE BELOW

def sum_of_digits(n: int) -> int:
    sum = 0
    if n < 10:
        sum += n # if only one digit.
    else:
        sum += (n % 10) + sum_of_digits(n // 10) #remainder of n/10 + n/10.
    return sum

print(sum_of_digits(4444))

def count_occurrences(data_list, target) -> int:
    count = 0
    if not data_list: #is empty
        count = 0
    else:
        if data_list[0] == target:
            count += 1 + count_occurrences(data_list[1:], target) # data_list(from 1 to end), target. this slices the data after postion 0
        else:
            count += count_occurrences(data_list[1:], target)
    return count

print(count_occurrences([1, 5, 5, 4, 3, 2, 9, 0, 0, 0, 5], 5))


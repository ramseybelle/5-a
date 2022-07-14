def multiply(n1, n2):
    if n2 == 0:  # base case, if n2 is 0
        return 0  # then return 0
    else:  # recursive case
        return n1 + multiply(n1, n2 - 1)  # n1 times n2 = n1 + (n1 times (n2-1))


# Testing the function . ignore/remove the code below if not needed
num1 = int(input("Enter a positive integer: "))
num2 = int(input("Enter another positive integer: "))
print("product of", num1, "and", num2, "is", multiply(num1, num2))

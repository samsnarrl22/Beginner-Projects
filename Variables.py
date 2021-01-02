# Variables let you store info that you can then use later
one = 1
two = 2
three = 3

print(one, two, three)
two = 4  # Integer
# The information stored inside the variable can be re-assigned
print(one, two, three)

Decimal = 1.1  # Float
print(Decimal)

StringVar = "Hello"  # String
print(StringVar)

# StringVar = StringVar + 1  will result in an error
StringVar = StringVar + "1"
print(StringVar)

# All these variables are global variables which is useful for constants for example pi = 3.14
# Local variables are within a function and can only be recalled in this function


def function_name():
    local_var = "World"
    print(one)  # this is a global variable so it can be recalled anywhere
    print(local_var)  # this is a local variable so it can only be recalled in the function
    return

# print(local_var) this results in an error as it is a local variable


function_name()

four, five, six = 4, 5, 6
print(four)
print(five)
print(six)

ten = four + six
print(ten)

# 11 = eleven this will result in an error
# left is what you're giving the value to
# right is what the value is

count = 7
print(count)
count = count + 1
print(count)
count += 1
print(count)
count = count * 3
print(count)
count *= 3
print(count)
count /= 81
print(count)
count -= 5
print(count)


# print(bin(17))
# print(oct(17))
# print(hex(17))

# print(f"An arbitrary number in binary: {bin(17)}")
##It will display the number as 0b10001. The 0b prefix is a way to remind you that this is a binary number.
##If you prefer to not see that prefix, you could type.
# print(f"An arbitrary number in binary without a prefix: {17:b}")

# How about hexadecimal and octal?
# print(f"An arbitrary number in octal: {oct(17)}")
# print(f"An arbitrary number in octal without a prefix: {17:o}")
# print(f"An arbitrary number in hexadecimal: {hex(17)}")
# print(f"An arbitrary number in hexadecimal without a prefix: {17:x}")

## Note that functions work alone, but the format specifiers don't:
## This works:
# exampleVar = bin(6)
# print(f"The value is {exampleVar}.")
# # This won't work:
# exampleVar = {6:b}
# print(f"The value is {exampleVar}.")


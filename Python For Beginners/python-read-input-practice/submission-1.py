def add_two_numbers() -> int:
    original = input()
    split_string = original.split(",")
    return int(split_string[0]) + int(split_string[1])

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())

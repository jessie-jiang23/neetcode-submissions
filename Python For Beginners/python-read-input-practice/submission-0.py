def add_two_numbers() -> int:
    original = input()
    split_string = original.split(",")
    result = 0
    for i in split_string:
        result += int(i)
    return result

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())

from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    my_list = {}
    for char in word:
        if char in my_list:
            my_list[char] += 1
        else:
            my_list[char] = 1
    return my_list


# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))

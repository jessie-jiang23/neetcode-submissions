from typing import List

def read_integers() -> List[int]:
    input_list = input()
    split_list = input_list.split(",")
    results = list()
    for i in split_list:
        results.append(int(i))
    return (results)

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())

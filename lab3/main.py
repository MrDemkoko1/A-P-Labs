example_set = {3, 1, -32, 5, 11, -4, 10, 9}
example_list = [5, 18, -3, -2, 12, 6, 5, 8]
example_tuple = (1, -3)


def find_third_biggest_element(x):

    ordered_list = list(x)

    if len(x) < 3:
        return 'there is no such number. Your array is too short'

    for element in range(len(ordered_list)):
        for next_element in range(element + 1, len(ordered_list)):
            if ordered_list[element] >= ordered_list[next_element]:
                ordered_list[element], ordered_list[next_element] = ordered_list[next_element], ordered_list[element]

    return(ordered_list[-3])

find_third_biggest_element(example_set)

print(f'Third biggest number in your array {example_set} is: {find_third_biggest_element(example_set)}')
print(f'Third biggest number in your array {example_list} is: {find_third_biggest_element(example_list)}')
print(f'Third biggest number in your array {example_tuple} is: {find_third_biggest_element(example_tuple)}')
example_set = {3, 1, -32, 5, 11, -4, 10, 9}

def find_third_bigger_element(x):

    ordered_list = list(x)

    for element in range(len(ordered_list)):
        for next_element in range(element + 1, len(ordered_list)):
            if ordered_list[element] >= ordered_list[next_element]:
                ordered_list[element], ordered_list[next_element] = ordered_list[next_element], ordered_list[element]

    return(ordered_list[2])

find_third_bigger_element(example_set)

print(f'Third bigger number in your array {example_set} is: {find_third_bigger_element(example_set)}')
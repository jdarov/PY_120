"""
For a list of numbers [1,2,3,3,4], return the highest sum of any set of consecutive numbers
ex [1,2,3,3,4] = 3+4 = 7 (1+2+3 = 6 < 7)

C
    input: list of ints
    output: int

    explicit:
        find the highest sum of consecutive ints
        ints stop being consecutive if any number repeats 
        all ints must be unique in a list
    implicit:
        empty list returns 0
O
# print(highest_sum([1,2,3,3,4] == 7))
# print(highest_sum([]) == 0)
# print(highest_sum([1,2,3,4,5,5,6,7,8,8,9,10] == 27))
D
    data: lists, ints

    functions:
        iterate through the list of ints starting at first int
            add numbers to a new list until reaching a repeat number
                add this list to list holding these lists
            reset the list of consecutive ints
        start again from the next int in the list

        return this list of consecutive int lists
    algo:
        create a list of all consecutive int lists in a list of ints
        iterate through these lists
        find the sum of each list
        return the maximum of all these sums
E
"""

def list_of_consecutive_ints(list_of_ints):

    list_of_c_ints = list()

    for x in range(len(list_of_ints)):
        repeated_ints = set()
        c_ints = list()
        for y in range(x, len(list_of_ints)):
            if list_of_ints[y] in repeated_ints:
                break
            repeated_ints.add(list_of_ints[y])
            c_ints.append(list_of_ints[y])
        list_of_c_ints.append(c_ints)
            
    
    return list_of_c_ints

def highest_sum(list_of_ints):
    return (max(sum(sublist) for sublist in list_of_consecutive_ints(list_of_ints))
            if list_of_ints else 0)

print(list_of_consecutive_ints([1,2,3,3,4]))
print(highest_sum([1,2,3,3,4]) == 7)
print(highest_sum([]) == 0)
print(highest_sum([1,2,3,4,5,5,6,7,8,8,9,10]) == 27)

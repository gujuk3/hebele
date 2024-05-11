def set_difference(set1, set2):
    # Find elements in set1 but not in set2
    difference1 = set1.difference(set2)

    # Find elements in set2 but not in set1
    difference2 = set2.difference(set1)

    return difference1, difference2


if __name__ == "__main__":
    # Taking input sets from the user
    input_set1 = input("Enter elements of the first set separated by spaces: ").split()
    input_set2 = input("Enter elements of the second set separated by spaces: ").split()

    # Converting input lists to sets
    set1 = set(input_set1)
    set2 = set(input_set2)

    # Finding the differences
    diff1, diff2 = set_difference(set1, set2)

    # Outputting the differences
    print("Elements in set1 but not in set2:", diff1)
    print("Elements in set2 but not in set1:", diff2)

""" Python 3 required ! """

def generate_array_chunk():
    """ Generate Y elements from user input of given length """
    line_str = input()
    chunk = [int(num) for num in line_str.strip().split()]
    return chunk


def generate_multidimensional_array(size):
    """ Generate Matrix with X*Y elements of given size """
    multidimensional_array = []
    for i in range(size):
        one_chunk = generate_array_chunk()
        while len(one_chunk) != size:
            one_chunk = generate_array_chunk()
        multidimensional_array.append(one_chunk)
    return multidimensional_array


def pop_top(multidimensional_array):
    """ Removes and returns the first item in the list
        Complexity: O(k) (k represents the number passed in as an argument for pop)
    """
    return multidimensional_array.pop(0)


def pop_left(multidimensional_array):
    """ Removes and returns last elements of each chunk
        Complexity: O(n)*O(1) (pop last - O(1), iterate over chunk O(n))
    """
    left_items = []
    for chunk in multidimensional_array:
        left_items.append(chunk.pop())
    return left_items


def pop_bottom(multidimensional_array):
    """ """
    return reversed(multidimensional_array.pop())


def pop_right(multidimensional_array):
    """ Reverse remaining matrix, removes and returns first element from each chunk
        Complexity: O(n) - to reverse * O(n) - to iterate * O(K) - to pop first element,
        (k represents the number passed in as an argument for pop)
    """
    right_items = []
    multidimensional_array = reversed(multidimensional_array)
    for chunk in multidimensional_array:
        right_items.append(chunk.pop(0))
    return right_items


def main():
    """ """
    size = input()
    size = int(size.strip())

    result = []
    if size >= 100:
        print('Number should be < 100. Try again')
    else:
        array = generate_multidimensional_array(size)
        while array:
            try:
                result.extend(pop_top(array))
                result.extend(pop_left(array))
                result.extend(pop_bottom(array))
                result.extend(pop_right(array))
            except IndexError:
                pass
    return result


result = main()
for item in result:
    print(item, end=" ")

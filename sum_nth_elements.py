# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


#  O(n)
# Проверяем остаток от деления - если 0, значит, суммируем.
sum_a = sum([number for number in range(1, 1000) if number % 3 == 0 or number % 5 == 0])


# O = O(n / 3)
# Берем каждый 3 елемент и складываем с каждым 5м елементом последовательности
def func(n, m, arr):
    left_step = n
    right_step = m
    # Последовательность уникальных елементов: каждого 3го и 5го
    items_to_sum = set()
    while n <= len(arr):
        items_to_sum.add(arr[n - 1])
        n += left_step
        if m >= len(arr):
            continue
        items_to_sum.add(arr[m - 1])
        m += right_step
    return sum(items_to_sum)

sum_b = func(3, 5, list(range(1, 1000)))


assert sum_a == sum_b, '{} is not equal {}'.format(sum_a, sum_b)
print(sum_a, sum_b)
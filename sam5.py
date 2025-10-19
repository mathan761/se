def sum_even_numbers(number_list):
    total_sum = 0
    for number in number_list:
        if isinstance(number, int) and number % 2 == 0:
            total_sum += number
    return total_sum

list_a = [10, 5, 2, 1, 8, 3]
result_a = sum_even_numbers(list_a)
print(result_a)

list_b = [1, 3, 5, 7, 9]
result_b = sum_even_numbers(list_b)
print(result_b)

list_c = [-4, 0, 11, -6, 1]
result_c = sum_even_numbers(list_c)
print(result_c)
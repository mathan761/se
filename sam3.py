from collections import Counter

def get_top_three_counts(digit_string):
    int_list = [int(digit) for digit in digit_string]
    count_dict = Counter(int_list)
    top_three = count_dict.most_common(3)
    sorted_top_three = sorted(top_three, key=lambda item: item[0])
    result_dict = dict(sorted_top_three)
    return result_dict

test_string = "112333444455555678900" 
result = get_top_three_counts(test_string)
print(result)
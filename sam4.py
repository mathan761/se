def get_entry_exit_slice(tpl, element_id):
    indices = [i for i, x in enumerate(tpl) if x == element_id]
    num_occurrences = len(indices)
    
    if num_occurrences < 1:
        return tuple()
    
    if num_occurrences == 1:
        first_index = indices[0]
        return tpl[first_index:]
    
    if num_occurrences >= 2:
        first_index = indices[0]
        second_index = indices[1]
        return tpl[first_index : second_index + 1]

print(get_entry_exit_slice((1, 2, 3), 8))
print(get_entry_exit_slice((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(get_entry_exit_slice((1, 2, 8, 5, 1, 2, 9), 8))
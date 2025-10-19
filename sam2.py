def remove_first_occurrence(tpl, element):
    try:
        index_to_remove = tpl.index(element)
        new_tpl = tpl[:index_to_remove] + tpl[index_to_remove + 1:]
        return new_tpl
    except ValueError:
        return tpl

print(remove_first_occurrence((1, 2, 3), 1))
print(remove_first_occurrence((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(remove_first_occurrence((2, 4, 6, 6, 4, 2), 9))
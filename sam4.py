def change_grades(grades: list[int]) -> list[int]:
    grades = [4 if i == 3 else i for i in grades if i  != 2]
    return grades

print(change_grades([2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]))
print(change_grades([4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]))
print(change_grades([5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]))


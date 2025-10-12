results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

results.sort()

print(f"3 Наихудших результата: {results[-3:]}")
print(f"3 Наилучших результата: {results[:3]}")
results_over_than_10 = [i for i in results if i >= 10]
print(f"Все результаты больше чем 10{results_over_than_10}")
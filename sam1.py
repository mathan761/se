from datetime import datetime
from math import sqrt

def main(kwargs):
    for key, value in kwargs.items():
        result = sqrt(value[0]**2 + value[1]**2)
        print(result)

if __name__ == '__main__':
    start_time = datetime.now()
    
    data = {
        'one': [10, 3],
        'two': [5, 4],
        'three': [15, 13],
        'four': [93, 53],
        'five': [133, 15]
    }
    
    main(data)
    
    time_costs = datetime.now() - start_time
    print(f"Время выполнения программы: {time_costs}")
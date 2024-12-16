import sys
from os import makedirs

def get_numbers(path):
    numbers = []
    with open(path, mode='r') as file:
        numbers = file.read()
    return numbers.split('\n')

def sort_numbers(numbers):
    sorted_numbers = sorted([int(num) for num in numbers])
    return sorted_numbers

def save_sorted_numbers(path, numbers):
    with open(path, mode='w+') as file:
        file.write("\n".join([str(num) for num in numbers]))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise ValueError("Not enough arguments.")
    catalog = sys.argv[1]
    file_name = sys.argv[2]
    makedirs(f"./{catalog}/sorted/", exist_ok=True)
    numbers = get_numbers(f"./{catalog}/unsorted/{file_name}")
    sorted_numbers = sort_numbers(numbers)
    save_sorted_numbers(f"./{catalog}/sorted/{file_name}", sorted_numbers)
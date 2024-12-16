import random
import sys
from os import makedirs

def generate_numbers(len):
    return [random.randint(0, 10000000) for _ in range(len)]

def save_generated_numbers(path, numbers):
    with open(path, mode='w+') as file:
        file.write("\n".join([str(num) for num in numbers]))

if __name__ == '__main__':
    if len(sys.argv) < 4:
        raise ValueError("Not enough arguments.")
    catalog = sys.argv[1]
    count_files = int(sys.argv[2])
    len_numbers = int(sys.argv[3])
    makedirs(f"./{catalog}/unsorted/", exist_ok=True)
    for file in range(count_files):
        numbers = generate_numbers(len_numbers)
        save_generated_numbers(f"./{catalog}/unsorted/{file}.txt", numbers)
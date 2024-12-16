import subprocess
import sys
import time 
from os import listdir

if len(sys.argv) < 4:
    raise ValueError("Not enough arguments.")
start = time.time()
catalog = sys.argv[1]
count_files = sys.argv[2]
len_numbers = sys.argv[3]

try:
    process = subprocess.run(["python", 'generate_numbers.py'] + [catalog, count_files, len_numbers], check=True)
except subprocess.CalledProcessError as e:
    raise Exception(e)

files = listdir(F"./{catalog}/unsorted")
for ind in range(int(count_files)):
    try:
        process = subprocess.run(["python", 'sort_numbers.py'] + [catalog, files[ind]], check=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e)

end = time.time()
print(f"{end - start} сек.")
import time
import random


start = time.time()
random.sample(range(10000000), k=100000).sort()
spent = str(time.time() - start)
file_name = time.strftime('%H.%M.%S %d.%m.%Y') + ".txt"
with open(file_name, "w", encoding="UTF-8") as f:
    f.write(spent)

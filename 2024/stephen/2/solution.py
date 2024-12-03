import sys

levels = []
error_threshold = 1
safe_sum = 0

with open(sys.argv[1]) as f:
    for line in f.readlines():
        s = line.split()
        if s:
            levels.append([int(i) for i in s])


for row in levels:
    errors = 0
    increasing = row[0] < row[1]
    
    for i in range(0, len(row)-1):
        if increasing:
            diff = row[i+1] - row[i]
        else:
            diff = row[i] - row[i+1]
        
        if diff > 0 and diff < 4:
            continue
        else:
            errors += 1

    if errors > error_threshold:
        continue
    else:
        safe_sum += 1

print(safe_sum)

import sys

locations_1 = []
locations_2 = []

locations_count_2 = {}

with open(sys.argv[1]) as f:
    for line in f.readlines():
        s = line.split()
        locations_1.append(int(s[0]))
        locations_2.append(int(s[1]))

        if not locations_count_2.get(int(s[1]), {}):
            locations_count_2[int(s[1])] = 1
        else:
            locations_count_2[int(s[1])] += 1

sorted_1 = locations_1.sort()
sorted_2 = locations_2.sort()

print(locations_1)
print(locations_2)

sum = 0

for i in range(0, len(locations_1)):
    sum += abs(locations_1[i] - locations_2[i])

print(f"sum: {sum}")

similarity_score = 0

for n in locations_1:
    if locations_count_2.get(n, {}):
        similarity_score += n * locations_count_2[n]
 
print(f"similarity score: {similarity_score}")

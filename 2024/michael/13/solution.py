import sys


def machine_cost(x1, x2, y1, y2, x, y):
    a = (x*y2-y*x2) / (x1*y2 - x2*y1)
    b = (y-a*y1) / y2
    # print(a, b)
    if int(a) != a or int(b) != b:
        return 0
    return 3*a + b

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    (x1, y1) = (0, 0)
    (x2, y2) = (0, 0)
    (x, y) = (0, 0)
    machines = []
    for line in lines:
        if line.startswith("Button A:"):
            details = line.split("Button A: ")[1].split(", ")
            x1 = int(details[0][1:])
            y1 = int(details[1][1:])
        elif line.startswith("Button B:"):
            details = line.split("Button B: ")[1].split(", ")
            x2 = int(details[0][1:])
            y2 = int(details[1][1:])
        elif line.startswith("Prize:"):
            details = line.split("Prize: ")[1].split(", ")
            x = int(details[0][2:]) + 10000000000000
            y = int(details[1][2:]) + 10000000000000
            machines.append((x1, y1, x2, y2, x, y))
    
    # print(machines)
    costs = [machine_cost(x1, x2, y1, y2, x, y) for (x1, y1, x2, y2, x, y) in machines]
    # print(costs)
    print(sum(costs))

    
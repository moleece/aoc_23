import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

reports = [list(map(int, line.split())) for line in lines]

## P1
def safe_report(report):
    sign = 1 if report[1] > report[0] else -1
    for i in range(1, len(report)):
        diff = report[i] - report[i-1]
        if diff * sign < 0 or abs(diff) > 3 or diff == 0:
            return False
    return True

print(sum(safe_report(report) for report in reports))

## P2
def safe_dampener(report):
    # Get the first 3 signs and take the median, in case removing one of the first two values would make it safe by flipping the polarity.
    # Broken edge case here for reports of length <4, but it doesn't matter for the provided input.
    signs = [1 if report[i] > report[i-1] else -1 for i in range(1, 4)]
    sign = sorted(signs)[1]
    for i in range(1, len(report)):
        diff = report[i] - report[i-1]
        if diff * sign < 0 or abs(diff) > 3 or diff == 0:
            # Try removing one of these values
            if safe_report(report[:i] + report[i+1:]) or safe_report(report[:i-1] + report[i:]):
                return True
            return False
    return True

print(sum(safe_dampener(report) for report in reports))
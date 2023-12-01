'''
You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
'''
import sys


def parseLine(line):
    # No error handling
    total = 0
    for i in range(len(line)):
        if line[i].isdigit():
            total += int(line[i]) * 10
            break
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            total += int(line[i])
            return total
    return 0
    
def parseLine_p2(line):
    # No error handling
    digitMap = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    newLine = ''
    for i in range(len(line)):
        if line[i].isdigit():
            newLine += line[i]
        else:
            for d in digitMap:
                if line[i:].startswith(d):
                    newLine += digitMap[d]
    return int(newLine[0]) * 10 + int(newLine[-1])

if __name__ == '__main__':
    filename = sys.argv[1]
    f = open(filename, 'r')
    total = 0
    for line in f.readlines():
        total += parseLine_p2(line)
    print(total)

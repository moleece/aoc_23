import sys
from PIL import Image

def get_quad(i,j, width, height):
    if i < (height-1) / 2:
        if j < (width-1) / 2:
            return 'q1'
        elif j > (width-1) / 2:
            return 'q2'
    elif i > (height-1) / 2:
        if j < (width-1) / 2:
            return 'q3'
        elif j > (width-1) / 2:
            return 'q4'
    return 'q5'

def parse_bunny(line):
    pos, vel = line.split()
    pos = pos[2:].split(',')
    vel = vel[2:].split(',')
    return (int(pos[0]), int(pos[1]), int(vel[0]), int(vel[1]))


def step_and_display(step, bunnies, width, height):
    new_bunnies = []
    for (j,i,y,x) in bunnies:
        i = (i + x) % height
        j = (j + y) % width
        new_bunnies.append((j,i,y,x))
    grid = [['.' for _ in range(width)] for _ in range(height)]
    for (j,i,_,_) in new_bunnies:
        grid[i][j] = '#'
    # Save as a png picture
    if step > 6500 and step < 6700:
        img = Image.new('RGB', (width, height), color = 'white')
        pixels = img.load()
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '#':
                    pixels[j,i] = (0,0,0)
        img.save(f'imgs/output_{step}.png')
    return new_bunnies

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    bunnies = [parse_bunny(line) for line in lines]
    width = 101
    height = 103

    # P1
    quad_counts = {'q1': 0, 'q2': 0, 'q3': 0, 'q4': 0, 'q5': 0}
    for (j,i,y,x) in bunnies:
        endI = (i + 100*x) % height
        endJ = (j + 100*y) % width
        quad_counts[get_quad(endI,endJ,width,height)] += 1
    
    print(quad_counts)
    print(quad_counts['q1'] * quad_counts['q2'] * quad_counts['q3'] * quad_counts['q4'])

    # P2
    for t in range(7000):
        bunnies = step_and_display(t+1, bunnies, width, height)

# 28, 131, 234, 337, 440, 543, 646, 749, 852, 955, 1058, 1161, 1264, 1367, 1470, 1573, 1676, 1779, 1882, 1985, 2088, 2191, 2294, 2397, 2500, 2603, 2706, 2809, 2912, 3015, 3118, 3221, 3324, 3427, 3530, 3633, 3736, 3839, 3942, 4045, 4148, 4251, 4354, 4457, 4560, 4663, 4766, 4869, 4972, 5075, 5178, 5281, 5384, 5487, 5590, 5693, 5796, 5899, 6002, 6105, 6208, 6311, 6414, 6517, 6620, 6723, 6826, 6929, 7032, 7135, 7238, 7341, 7444, 7547, 7650, 7753, 7856, 7959, 8062, 8165, 8268, 8371, 8474, 8577, 8680, 8783, 8886, 8989, 9092, 9195, 9298, 9401, 9504, 9607, 9710, 9813, 9916, 10019, 10122, 10225, 10328, 10431, 10534, 10637, 10740, 10843, 10946, 11049, 11152, 11255, 11358, 11461, 11564, 11667, 11770, 11873, 11976, 12079, 12182, 12285, 12388, 12491, 12594, 12697, 12800, 12903, 13006, 13109, 13212, 13315, 13418, 13521 
# 55, 156, 257, 358, 459, 560, 661, 762, 863, 964, 1065, 1166, 1267, 1368, 1469, 1570, 1671, 1772, 1873, 1974, 2075, 2176, 2277, 2378, 2479, 2580, 2681, 2782, 2883, 2984, 3085, 3186, 3287, 3388, 3489, 3590, 3691, 3792, 3893, 3994, 4095, 4196, 4297, 4398, 4499, 4600, 4701, 4802, 4903, 5004, 5105, 5206, 5307, 5408, 5509, 5610, 5711, 5812, 5913, 6014, 6115, 6216, 6317, 6418, 6519, 6620, 6721, 6822, 6923, 7024, 7125, 7226, 7327, 7428, 7529, 7630, 7731, 7832, 7933, 8034, 8135, 8236, 8337, 8438, 8539, 8640, 8741, 8842, 8943, 9044, 9145, 9246, 9347, 9448, 9549, 9650, 9751, 9852, 9953, 10054, 10155, 10256, 10357, 10458, 10559, 10660, 10761, 10862, 10963, 11064, 11165, 11266, 11367, 11468, 11569, 11670, 11771, 11872, 11973, 12074, 12175, 12276, 12377, 12478, 12579, 12680, 12781, 12882, 12983, 13084, 13185, 13286,
# python 1.py input.txt
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str)
args = parser.parse_args()
with open(args.input_file, 'r') as f:
    lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()


def convert_image(image):
    image_array = []
    for row in image:
        image_array.append([])
        for i in range(len(row)):
            if row[i] == '.':
                image_array[-1].append(0)
            else:
                image_array[-1].append(1)
    
    return np.array(image_array)


def find_reflection_in_half(image_array_half, reflect_index):
    print(f"image array half: \n{image_array_half}")
    reflection_found = False
    reflection_index = -1
    for i in range(1, (len(image_array_half)//2)+1):
        array_sum = image_array_half[0:i] + image_array_half[i:i+i][::-1]
        reflection_found = not np.any(array_sum == 1)
        smudged_reflection_found = np.sum(array_sum == 1) == 1

        print('array sum')
        print(array_sum)
        
        # part 1
        # if reflection_found:
        # part 2
        if smudged_reflection_found:
            print('reflection found')
            if reflect_index:
                reflection_index = len(image_array_half) - i
            else:
                reflection_index = i

            return smudged_reflection_found, reflection_index

    return smudged_reflection_found, reflection_index

def calculate_value(reflection_index, orientation):
    value = 0
    if orientation == 'horizontal':
        value += reflection_index * 100
    if orientation == 'vertical':
        value += reflection_index

    return value


if __name__ == "__main__":
    images = [[]]
    image_arrays = []

    for line in lines:
        if len(line) == 0:
            images.append([])
        else:
            images[-1].append(line)

    count_vertical_rows_to_left = 0
    count_horizontal_rows_above = 0
    total = 0

    for image in images:
        image_arrays.append(convert_image(image))

    total = 0
    for image_array in image_arrays:
        reflection_found = False
        arrays = []
        horizontal_image_array = image_array
        horizontal_image_array_flipped = horizontal_image_array[::-1]
        vertical_image_array = image_array.T
        vertical_image_array_flipped = vertical_image_array[::-1]

        arrays.append(horizontal_image_array)
        arrays.append(horizontal_image_array_flipped)
        arrays.append(vertical_image_array)
        arrays.append(vertical_image_array_flipped)

        i = 0
        orientation = ''

        while i < 4 and not reflection_found:
            reflect_index = False
            if i in (1, 3):
                reflect_index = True

            image_array_half = arrays[i]
            reflection_found, reflection_index = find_reflection_in_half(image_array_half, reflect_index)
            if reflection_found:
                if i in (2, 3):
                    orientation = 'vertical'
                else: 
                    orientation = 'horizontal'

            i += 1

        total += calculate_value(reflection_index, orientation)

    print(f"total: {total}")


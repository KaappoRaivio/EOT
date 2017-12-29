from PIL import Image
import sys, os, string, random

try:
    path = sys.argv[2]
except IndexError:
    print('(c) Kaappo Raivio 2017')
    quit()
pwd = os.environ['PWD']

if path[0] != '/':
    path = pwd + '/' + path

class colors:
    black = '\033[30m'
    red = '\033[31m'
    yellow = '\033[33m'
    green = '\033[32m'
    cyan = '\033[36m'
    blue = '\033[34m'
    magenta = '\033[35m'
    white = '\033[37m'

def getColor(tuple):
    possible_colors = [colors.red, colors.yellow, colors.green, colors.cyan, colors.blue,  colors.magenta]
    try:
        huey = hue(tuple) * 60
    except TypeError:
        return colors.white
    if saturation(tuple) <= 0.1:
        return colors.white
    if huey >= 0 and huey < 30 or huey >= 330 and huey < 360:
        return possible_colors[0]
    elif huey >= 30 and huey < 90:
        return possible_colors[1]
    elif huey >= 90 and huey < 150:
        return possible_colors[2]
    elif huey >= 150 and huey < 210:
        return possible_colors[3]
    elif huey >= 210 and huey < 270:
        return possible_colors[4]
    elif huey >= 270 and huey < 330:
        return possible_colors[5]
    else:
        print(huey, tuple)
        raise(Exception)
def getCharacter(tuple):
    try:
        pixel_average = sum(tuple) // len(tuple)
    except TypeError:
        pixel_average = tuple
    chars = [[' ', '░', '▒', '▓', '█'], [' ', '▁', '▂', '▃', '▄', '▅', '▆', '▇', '█'], [' ', '⠠', '⠒', '⡉', '⡖', '⡶', '⣶', '⣽', '⣿', '█', '█', '█']]
    chars = [' ', '░', '▒', '▓', '█']
    tuple = [tuple[0], tuple[1], tuple[2]]
    for i in range(len(tuple)):
        tuple[i] = tuple[i] / 256
    huey = hue(tuple)
    for i in range(len(chars)):
        step = 256 // len(chars)
        if pixel_average in range(i * step, (i + 1) * step):
            return getColor(tuple) + chars[i] * 2
    return chars[0] * 2
def luminance(tuple):
    return (max(tuple) + min(tuple)) / 2
def saturation(tuple):
    if luminance(tuple) <= 0.5:
        return (max(tuple) - min(tuple)) / (max(tuple) + min(tuple))
    else:
        return (max(tuple) - min(tuple)) / (2.0 - max(tuple) - min(tuple))
def hue(tuple):
    try:
        if max(tuple) == tuple[0]:
            if (tuple[1] - tuple[2]) / (max(tuple) - min(tuple)) < 0:
                return (tuple[1] - tuple[2]) / (max(tuple) - min(tuple)) + 1
            else:
                return (tuple[1] - tuple[2]) / (max(tuple) - min(tuple))
        if max(tuple) == tuple[1]:
            if 2.0 + (tuple[2] - tuple[0]) / (max(tuple) - min(tuple)) < 0:
                return 2.0 + (tuple[2] - tuple[0]) / (max(tuple) - min(tuple)) + 1
            else:
                return 2.0 + (tuple[2] - tuple[0]) / (max(tuple) - min(tuple))
        if max(tuple) == tuple[2]:
            if 4.0 + (tuple[0] - tuple[1]) / (max(tuple) - min(tuple)) < 0:
                return 4.0 + (tuple[0] - tuple[1]) / (max(tuple) - min(tuple)) + 1
            else:
                4.0 + (tuple[0] - tuple[1]) / (max(tuple) - min(tuple))
    except ZeroDivisionError:
        return None
try:
    Im = Image.open(path)
except FileNotFoundError:
    print("Error: The file `{}' is non-existent".format(path))
    quit()
try:
    Im = Image.open(path)
except FileNotFoundError:
    print("Error: The file `{}' is non-existent".format(path))
    quit()

scaled_width = int(sys.argv[1]) // 2.00000


aspect_ratio = Im.size[0] / Im.size[1]
scaled_height = scaled_width // aspect_ratio



size = scaled_width, scaled_height

Im.thumbnail(size)


merkit = []

print('\e[34m')

pix = Im.load()
for a in range(Im.size[1]):
    temp = []
    for i in range(Im.size[0]):
        temp.append(getCharacter(pix[i, a]))
    print(''.join(temp))

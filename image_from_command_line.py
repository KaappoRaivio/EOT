width_correction_factor = 2
saturation = 0.2


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
    all = ['\033[31m', '\033[33m', '\033[32m', '\033[36m', '\033[34m', '\033[35m', '\033[37m']
    black = '\033[30m'
    red = '\033[31m'
    yellow = '\033[33m'
    green = '\033[32m'
    cyan = '\033[36m'
    blue = '\033[34m'
    magenta = '\033[35m'
    white = '\033[37m'

def getColor(hue):
    possible_colors = colors.all
    hue *= 60
    if hue >= 0 and hue < 30 or hue >= 330 and hue < 360:
        return possible_colors[0]
    elif hue >= 30 and hue < 90:
        return possible_colors[1]
    elif hue >= 90 and hue < 150:
        return possible_colors[2]
    elif hue >= 150 and hue < 210:
        return possible_colors[3]
    elif hue >= 210 and hue < 270:
        return possible_colors[4]
    elif hue >= 270 and hue < 330:
        return possible_colors[5]
    else:
        print(hue, tuple)
        raise(Exception)
def getCharacter(tuple):
    #tuplen arvot ovat välillä 0 .. 1
    chars = [' ', '░', '▒', '▓', '█']
    char = ''
    HSV = [getHue(tuple), getSaturation(tuple), getLuminance(tuple)]
    if HSV[0] == -1:
        assert(HSV[1] == 0)
    step = 1 / len(chars)
    for i in range(len(chars)):
        if HSV[2] > step * i and HSV[2] < step * (i + 1):
            char = chars[i]
    #print(HSV)
    if HSV[1] <= saturation:
        #print('hei')
        return colors.white + char * 2
    else:
        return getColor(HSV[0]) + char * 2

def getLuminance(tuple):
    return (max(tuple) + min(tuple)) / 2
def getSaturation(tuple):
    if getLuminance(tuple) >= 0.5:
        return (max(tuple) - min(tuple)) / (max(tuple) + min(tuple))
    else:
        return (max(tuple) - min(tuple)) / (2.0 - max(tuple) - min(tuple))
def getHue(tuple):
    try:
        if max(tuple) == tuple[0]:
            if (tuple[1] - tuple[2]) / (max(tuple) - min(tuple)) < 0:
                return (tuple[1] - tuple[2]) / (max(tuple) - min(tuple)) + 6
            else:
                return (tuple[1] - tuple[2]) / (max(tuple) - min(tuple))
        if max(tuple) == tuple[1]:
            if 2.0 + (tuple[2] - tuple[0]) / (max(tuple) - min(tuple)) < 0:
                return 2.0 + (tuple[2] - tuple[0]) / (max(tuple) - min(tuple)) + 6
            else:
                return 2.0 + (tuple[2] - tuple[0]) / (max(tuple) - min(tuple))
        if max(tuple) == tuple[2]:
            if 4.0 + (tuple[0] - tuple[1]) / (max(tuple) - min(tuple)) < 0:
                return 4.0 + (tuple[0] - tuple[1]) / (max(tuple) - min(tuple)) + 6
            else:
                return 4.0 + (tuple[0] - tuple[1]) / (max(tuple) - min(tuple))
    except ZeroDivisionError:
        return -1
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

scaled_width = int(sys.argv[1]) // width_correction_factor


aspect_ratio = Im.size[0] / Im.size[1]
scaled_height = scaled_width // aspect_ratio



size = scaled_width, scaled_height

Im.thumbnail(size)


merkit = []

pix = Im.load()
for a in range(Im.size[1]):
    temp = []
    for i in range(Im.size[0]):
        zero_to_one = []
        try:
            zero_to_one = [pix[i, a][0], pix[i, a][1], pix[i, a][2]]
        except TypeError:
            zero_to_one = [pix[i, a], pix[i, a], pix[i, a]]
        for i in range(len(zero_to_one)):
            zero_to_one[i] = zero_to_one[i] / 255
        temp.append(getCharacter(zero_to_one))
    print(''.join(temp))

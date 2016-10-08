
from PIL import Image
import pprint

def determine_octave_and_note(number):
    octave = number / 64
    note = (number % 64)*100 / 530
    result = {"octave": octave, "note": note, "duration": 1}
    return result


def parse_picture(path_image="test.jpeg", duration_step=5):
    im = Image.open(path_image, 'r')
    pix_val = list(im.getdata())

    R = []
    G = []
    B = []

    # Examples for R, G, B
    # R = [
    #   {note:0, octave:3, duration:5},
    #   {note:11, octave:0, duration:2}
    # ]

    for i in pix_val:
        R.append(determine_octave_and_note(i[0]))
        G.append(determine_octave_and_note(i[1]))
        B.append(determine_octave_and_note(i[2]))
        print(R)


parse_picture()

from PIL import Image
import pprint


def append_note(note_list, number):
    note = {
        "octave": number / 64,
        "note": (number % 64) * 100 / 533,
        "duration": 1
    }

    def same_note(x, y):
        return x["octave"] == y["octave"] and x["note"] == y["note"]

    if len(note_list) and same_note(note_list[-1], note):
        note_list[-1]["duration"] += 1
    else:
        note_list.append(note)


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

    print 'started processing image'
    for i in pix_val:
        append_note(R, i[0])
        append_note(G, i[0])
        append_note(B, i[0])
    print 'finished processing image'

    return R, G, B


if __name__ == '__main__':
    parse_picture()

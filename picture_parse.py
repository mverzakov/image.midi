from PIL import Image


def append_note(note_list, number):
    note = {
        "octave": number / 64,
        "note": (number % 64) * 100 / 533,
        "duration": 1
    }

    def same_note(x, y):
        return x["octave"] == y["octave"] and x["note"] == y["note"]

    seq = note_list['seq']

    if len(seq) and same_note(seq[-1], note):
        seq[-1]["duration"] += 1
    else:
        seq.append(note)
        if not note_list['min_length'] or len(seq) > 1 and note_list['min_length'] > seq[-2]["duration"]:
            note_list['min_length'] = seq[-1]["duration"]


def normalize_seq(note_list):
    result = []
    for note in note_list['seq']:
        length = int(
            round(
                float(note['duration']) / float(note_list['min_length'])
            )
        )
        durations = "{0:b}".format(length)
        base = 64
        for val in reversed(durations):
            if int(val):
                result.append(note)
                result[-1]['duration'] = float(1) / float(base)
            base /= 2
    return result


def parse_picture(path_image="test.jpeg", duration_step=5):
    im = Image.open(path_image, 'r')
    pix_val = list(im.getdata())

    R = {
        'min_length': 0,
        'seq': []
    }
    G = {
        'min_length': 0,
        'seq': []
    }
    B = {
        'min_length': 0,
        'seq': []
    }

    # Examples for R, G, B
    # R = [
    #   {note:0, octave:3, duration:5},
    #   {note:11, octave:0, duration:2}
    # ]
    for i in pix_val:
        append_note(R, i[0])
        append_note(G, i[1])
        append_note(B, i[2])

    return [normalize_seq(i) for i in R, G, B]


if __name__ == '__main__':
    parse_picture()

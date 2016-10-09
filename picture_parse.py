# -*- coding: utf-8 -*-
from PIL import Image


def append_note(note_list, number):
    """Append note to list or increase previous note duration."""
    notes = [0, 2, 4, 7, 9]

    note = {
        "octave": number / 64 + 3,
        "note": notes[(number % 64) * 10 / 128],
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
    """Change notes durations based on min_length."""
    result = []
    for note in note_list['seq']:
        length = int(
            round(
                float(note['duration']) / float(note_list['min_length'])
            )
        )
        durations = "{0:b}".format(length)
        base = 16.0
        for val in reversed(durations):
            if int(val):
                result.append(note.copy())
                result[-1]['duration'] = 1.0 / base
            base /= 2.0
    return result


def default_normalize_seq(note_list):
    """Change duration of all notes to 1/8."""
    for note in note_list['seq']:
        note['duration'] = 1.0 / 8.0
    return note_list['seq']


def parse_picture(path_image="test.jpeg", normalize=True):
    """Return list of notes sequences for each of colors."""
    im = Image.open(path_image, 'r')
    im.thumbnail([64, 64], Image.ANTIALIAS)
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
    normalize_func = normalize_seq if normalize else default_normalize_seq
    return [normalize_func(i) for i in R, G, B]

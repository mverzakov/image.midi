# -*- coding: utf-8 -*-
import argparse
import os

from audio_tools import make_music, play_music
from picture_parse import parse_picture


def extant_file(x):
    """'Type' for argparse - checks that file exists but does not open."""
    if not os.path.exists(x):
        raise argparse.ArgumentTypeError("{0} does not exist".format(x))
    return x


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image to midi converter")
    parser.add_argument("-i", "--input", dest="filename", required=True,
                        type=extant_file, help="input image file",
                        metavar="FILE")
    parser.add_argument("--normalize", dest='normalize', default=False,
                        action="store_true", help="Flag to normalize")
    parser.add_argument("--play", dest='play', default=False,
                        action="store_true", help="Flag to play sound")
    args = parser.parse_args()
    result = parse_picture(path_image=args.filename, normalize=args.normalize)
    filename = args.filename.split('/')[-1].split('.')[-2]
    music_file = make_music(result, [3, 4, 53], name=filename)
    if args.play:
        play_music(music_file)


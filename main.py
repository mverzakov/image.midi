from audio_tools import make_music
from picture_parse import parse_picture

result = parse_picture(path_image='/home/maxim/1.png')
make_music(result, [40, 14, 9])
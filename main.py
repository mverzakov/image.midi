from audio_tools import make_music
from picture_parse import parse_picture

result = parse_picture(path_image='images/Logo.png')
make_music(result, [95, 108, 125])
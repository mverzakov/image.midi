# -*- coding: utf-8 -*-
import pygame
from pyknon.genmidi import Midi
from pyknon.music import NoteSeq, Note
from datetime import datetime


def make_music(notes_tracks, instruments, name='default', tempo=120):
    midi = Midi(tempo=tempo,
                number_tracks=len(notes_tracks),
                instrument=instruments)
    for i, notes in enumerate(notes_tracks):
        midi.seq_notes(dict_to_notes(notes), track=i)
    name = "midi/{}-{}.midi".format(name, datetime.now())
    midi.write(name)
    return name


def dict_to_notes(notes, volume=120):
    result = NoteSeq()
    for note in notes:
        pitch = note['note']
        octave = note['octave']
        duration = note['duration']
        volume = volume
        result.append(Note(pitch, octave, duration, volume))
    return result


def play_music(music_file):
    """
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    """
    freq = 44100  # audio CD quality
    bitsize = -16  # unsigned 16 bit
    channels = 2  # 1 is mono, 2 is stereo
    buffer = 1024  # number of samples
    pygame.mixer.init(freq, bitsize, channels, buffer)
    # optional volume 0 to 1.0
    pygame.mixer.music.set_volume(0.8)
    try:
        clock = pygame.time.Clock()
        try:
            pygame.mixer.music.load(music_file)
            print "Music file %s loaded!" % music_file
        except pygame.error:
            print "File %s not found! (%s)" % (music_file, pygame.get_error())
            return
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            # check if playback has finished
            clock.tick(30)
    except KeyboardInterrupt:
        # if user hits Ctrl/C then exit
        # (works only in console mode)
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.stop()
        raise SystemExit


import json
import os

TRACKS_FILE = "played_tracks.json"

def load_flags():
    if os.path.exists(TRACKS_FILE):
        with open(TRACKS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_flags(flags):
    with open(TRACKS_FILE, 'w') as f:
        json.dump(flags, f)

def flag_song(emotion, song_path):
    flags = load_flags()
    played = flags.get(emotion, [])
    if song_path not in played:
        played.append(song_path)
        flags[emotion] = played
        save_flags(flags)

def get_next_song(emotion, song_list):
    flags = load_flags()
    played = flags.get(emotion, [])

    for song in song_list:
        if song not in played:
            flag_song(emotion, song)
            return song

    # All played, reset and start over
    flags[emotion] = []
    save_flags(flags)
    return song_list[0]

#!/usr/bin/env python3
import json
import subprocess
import sys

def get_media_info():
    try:
        player_list = subprocess.check_output(['playerctl', '--list-all']).decode('utf-8').strip().split('\n')
        if not player_list:
            return None

        player = player_list[0]  # Take the first available player
        metadata = subprocess.check_output(['playerctl', 'metadata', '--format', '{{ artist }} - {{ title }}'], universal_newlines=True)
        status = subprocess.check_output(['playerctl', 'status'], universal_newlines=True).strip()
    except subprocess.CalledProcessError:
        return None

    return {
        'text': metadata.strip(),
        'class': 'custom-' + player,
        'alt': player
    }

media_info = get_media_info()

if media_info is not None:
    print(json.dumps(media_info))
else:
    print(json.dumps({'text': 'No media'}))
sys.stdout.flush()

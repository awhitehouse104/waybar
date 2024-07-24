#!/usr/bin/env python3
import json
import subprocess
import sys

def get_media_info():
    try:
        metadata = subprocess.check_output(['playerctl', 'metadata', '--format', '{{ artist }} - {{ title }}'])
        status = subprocess.check_output(['playerctl', 'status']).decode('utf-8').strip()
        player = subprocess.check_output(['playerctl', '--list-all']).decode('utf-8').strip().split('\n')[0]
    except subprocess.CalledProcessError:
        return None

    return {
        'text': metadata.decode('utf-8').strip(),
        'class': 'custom-' + player,
        'alt': player
    }

media_info = get_media_info()

if media_info is not None:
    print(json.dumps(media_info))
else:
    print(json.dumps({'text': 'No media'}))
sys.stdout.flush()

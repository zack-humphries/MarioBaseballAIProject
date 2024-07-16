import os.path
import time
from memory_watcher import *

def find_dolphin_dir():
    candidates = ['~/.dolphin-emu', '~/.local/share/.dolphin-emu']

    for candidate in candidates:
        path = os.path.expanduser(candidate)
        if os.path.isdir(path):
            return path
    return None


def write_locations(dolphin_dir, locations):
    path = dolphin_dir + 'MemoryWatcher/Locations.txt'
    with open(path, 'w') as f:
        f.write('\n'.join(locations))

        dolphin_dir = find_dolphin_dir()
        if dolphin_dir is None:
            print('Could not detect dolphin directory')
            return
        

def run(state, sm, memoryWatcher pad, stats):
    while True:
        last_frame = state.frame
        res = next(memoryWatcher)
        if res is not None:
            sm.handle(*res)
            if state.frame > last_frame:
                stats.add_frames(state.frame - last_frame)
                start = time.time()
                
        
from itertools import *
import re
import numpy as np
from datetime import datetime

time_fmt = '%Y-%m-%d %H:%M'

timestamp_re = '\[(.+)\]'
timestamp_re = re.compile(timestamp_re)
sleep_re = re.compile(r'.*asleep')
wake_re = re.compile(r'.*wakes up')
shift_re = re.compile(r'.*Guard #(\d+) begins shift')

class Event:
    def __init__(self, timestamp):
        self.timestamp = timestamp

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, str(self.timestamp))

class Shift(Event):
    def __init__(self, timestamp, id):
        super().__init__(timestamp)
        self.id = id

class Sleep(Event):
    pass

class Wake(Event):
    pass

def read_lines():
    import sys
    raw = sys.stdin.read()

    for line in raw.splitlines():
        if not line: continue
        yield line

def read_events():
    for line in read_lines():
        match = timestamp_re.match(line)
        timestamp = match.groups()[0]
        timestamp = datetime.strptime(timestamp, time_fmt)
        if shift_re.match(line):
            id = shift_re.match(line).groups()[0]
            event = Shift(timestamp, id)
        elif wake_re.match(line):
            event = Wake(timestamp)
        elif sleep_re.match(line):
            event = Sleep(timestamp)
        yield event


def determine_roster(events):
    ids = set(event.id for event in events if isinstance(event, Shift))
    ids = sorted(list(ids))
    roster = {id: np.zeros(60, dtype=int) for id in ids}

    current_id = None
    sleep_t = 0
    for event in events:
        if isinstance(event, Shift):
            current_id = event.id
        elif isinstance(event, Sleep):
            sleep_t = event.timestamp.minute
        elif isinstance(event, Wake):
            wake_t = event.timestamp.minute
            roster[current_id][sleep_t:wake_t] += 1

    return roster


def part_one():
    events = list(read_events())
    events = sorted(events, key=lambda event: event.timestamp)
    roster = determine_roster(events)

    # Why does Python not have a pretty argmax
    most_slept = max(sum(minutes) for minutes in roster.values())
    max_id = next(id for id, minutes in roster.items() if sum(minutes) == most_slept)

    print(max_id)
    sleepiest_minute = np.argmax(roster[max_id])
    print(sleepiest_minute)
    print(int(max_id) * sleepiest_minute)


def part_two():
    events = list(read_events())
    events = sorted(events, key=lambda event: event.timestamp)
    roster = determine_roster(events)

    most_slept = max(np.max(minutes) for id, minutes in roster.items())

    for id, minutes in roster.items():
        if np.max(minutes) == most_slept:
            which_minute = np.argmax(minutes)
            print(id)
            print(which_minute)
            print(int(id) * which_minute)
            break


if __name__ == "__main__":
    part_two()

from datetime import datetime
import numpy as np
import re

# read stuff
FORMAT = '%Y-%m-%d %H:%M'
regex = ('\[(?P<ts>(?P<Y>\d{4})-(?P<m>\d{2})-(?P<d>\d{2}) '
         '(?P<H>\d{2}):(?P<M>\d{2}))\] (?P<msg>.+)')
p = re.compile(regex)
data = []
guard_ids = {}
n_guards = 0
with open('input.txt') as f:
    for l in f:
        match = p.match(l).groupdict()
        data.append((datetime.strptime(match['ts'], FORMAT),
                     match['msg']))
        # put all guard id into a dict
        if 'Guard #' in match['msg']:
            gid = int(match['msg'].split(' ')[1][1:])
            guard_ids[gid] = n_guards
            n_guards += 1

# sort record
data.sort(key=lambda x: x[0])

current_guard = None
asleep = None
guards_sleep_record = np.zeros((n_guards, 60))

for ts, msg in data:
    if 'Guard #' in msg:
        current_guard = int(msg.split(' ')[1][1:])
    elif msg == 'falls asleep':
        asleep = ts
    elif msg == 'wakes up':
        guards_sleep_record[guard_ids[current_guard],
                            asleep.minute:ts.minute] += 1

# get row with the maximum sum
max_sum_id = np.argmax(guards_sleep_record.sum(1))
# get guards of that maximum sum
guard_id = [gid for gid, c in guard_ids.items() if c == max_sum_id][0]
# get maximum sleep of a minute
max_col_val = np.argmax(guards_sleep_record[max_sum_id])
print('Part 1:', guard_id * max_col_val)

# get maximum sleep time of a minute
max_slept = np.max(guards_sleep_record)
# get guard id of that
inds = np.where(guards_sleep_record == max_slept)
guard_id = [gid for gid, c in guard_ids.items() if c == inds[0][0]][0]
print('Part 2:', guard_id * inds[1][0])

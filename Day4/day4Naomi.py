import re
import datetime as dt
from operator import itemgetter
from collections import defaultdict
import numpy as np

regex = "\[(?P<yy>\d+)-(?P<mm>\d+)-(?P<dd>\d+) (?P<hh>\d+):(?P<min>\d+)\] (?P<event>.*)"
p = re.compile(regex)

file = 'Day4/input.txt'
log = []

with open(file,'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        match = {k: v for k, v in p.match(line).groupdict().items()}
        time = dt.datetime(int(match['yy']),int(match['mm']),int(match['dd']),int(match['hh']),int(match['min']))
        minute=int(match['min'])
        event = match['event']
        log.append(dict(t=time,ev=event,minute=minute))
log_sorted = sorted(log, key=itemgetter('t'))

asleep = defaultdict(lambda:np.zeros(60))

while len(log_sorted)>0:
    guard_id = re.search('\d+',log_sorted[0]['ev']).group(0)
    sleeptimes = np.zeros(60)
    counter = 1
    while (re.search('Guard',log_sorted[counter]['ev'])==None):
        counter +=1
        if len(log_sorted)==counter:
            break
    for i in range(0,(counter-1)//2):
        sleep = log_sorted[2*i+1]['minute']
        wake = log_sorted[2*i+2]['minute']
        sleeptimes[sleep:wake]+=1
    asleep[guard_id]+=sleeptimes
    del log_sorted[0:counter]

totalasleep = [dict(id=row, tot=sum(asleep[row])) for row in asleep.keys()]
totalsorted= sorted(totalasleep, key=itemgetter('tot'),reverse=True)

maxid = totalsorted[0]['id']
maxminute = np.argmax(asleep[maxid])
print(int(maxid)*maxminute)

trackmax=0
answer=0
idanswer=0
for row in asleep.keys():
    if np.max(asleep[row])>=trackmax:
        trackmax=max(asleep[row])
        answer=np.argmax(asleep[row])
        idanswer=row

print(answer*int(idanswer))

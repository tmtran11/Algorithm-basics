import urllib.request
from operator import itemgetter
text = urllib.request.urlopen("http://www.udacity.com/file?file_key=agpzfnVkYWNpdHl1ckALEgZDb3Vyc2UiBWNzMjE1DAsSCUNvdXJzZVJldhgBDAsSBFVuaXQY-qsODAsSDEF0dGFjaGVkRmlsZRiskBIM")
all = []
for l in text:
    line = str(l[:-1])[2:-1].split(',')
    if line[1] == 'F':
        line[2] = int(line[2])
        all.append(line)
result = sorted(all, key=itemgetter(2))
print(result[-2])

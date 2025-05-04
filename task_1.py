time_str = '1h 45m,360s,25m,30m 120s,2h 60s'
time_parts = time_str.split(',')
time_sum = 0

for part in time_parts:
    time = part.split()
    minutes = 0
    for t in time:
        if 'h' in t:
            hours = int(t.replace('h', ''))
            minutes += hours * 60
        elif 'm' in t:
            minutes += int(t.replace('m', ''))
        elif 's' in t:
            seconds = int(t.replace('s', ''))
            minutes += seconds // 60
    time_sum += minutes

print(time_sum)         
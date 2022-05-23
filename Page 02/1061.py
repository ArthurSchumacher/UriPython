initial_day = int(input().split()[1])

hour = input().split(':')
initial_hour = int(hour[0])
initial_minutes = int(hour[1])
initial_seconds = int(hour[2])

final_day = int(input().split()[1])

hour = input().split(':')
final_hour = int(hour[0])
final_minutes = int(hour[1])
final_seconds = int(hour[2])

durationInSeconds = ((final_day * 86400 + final_hour * 3600 + final_minutes * 60 + final_seconds) - (initial_day * 86400 + initial_hour * 3600 + initial_minutes * 60 + initial_seconds))

days = durationInSeconds // 86400
hours = (durationInSeconds // 3600) % 24
minutes = (durationInSeconds // 60) % 60
seconds = durationInSeconds % 60

print(days, 'dia(s)')
print(hours, 'hora(s)')
print(minutes, 'minuto(s)')
print(seconds, 'segundo(s)')
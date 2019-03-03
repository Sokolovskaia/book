timetable = {
    'SU 2380': 'Женева',
    'SU 1162': 'Ростов-на-Дону',
    'SU 2124': 'Салоники',
}

print(timetable['SU 2124'])

timetable['SU 2124'] = 'Пакистан'
print(timetable)



timetable['SU 2596'] = 'Венеция'
print(timetable)

print('SU 2596' in timetable)

for key in timetable:
    print(key, end=' ')
    print(timetable[key])


for key, value in timetable.items():
    print(key, value)
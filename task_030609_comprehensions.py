work_hours = [8, 8, 8, 12, 4, 7, 8, 9, 8, 10, 6, 11]
overdue_work_hours = []

for hours in work_hours:
    if hours > 8:
        overdue_work_hours.append(hours)

# С помощью list comprehension можно реализовать эту логику в одну строку:
overdue_work_hours2 = [hours for hours in work_hours if hours > 8]

print(overdue_work_hours, '\n', overdue_work_hours2)

work_hours_per_weeks = [[8, 8, 8, 12, 4], [7, 8, 9, 8, 10], [6, 11, 8, 8, 9]]

# Можно свернуть в list comprehension и цикл с большим количеством вложенностей.
# Однако в таком виде конструкция уже становится нечитаемой.
overdue_work_hours3 = [hours for week_hours in work_hours_per_weeks for hours in week_hours if hours > 8]

# Можно немного улучшить читаемость, если оформить код в несколько строк:
overdue_work_hours4 = [
    hours
    for week_hours in work_hours_per_weeks
    for hours in week_hours
    if hours > 8
]

print(overdue_work_hours3, '\n', overdue_work_hours4)


# Генераторы множеств формируются аналогично спискам:
work_hours = [8, 8, 8, 12, 4, 7, 8, 9, 8, 10, 6, 11]
overdue_work_hours5 = {hours for hours in work_hours if hours > 8}
print(overdue_work_hours5)


#А для словаря нужно формировать пары ключей-значений:
work_hours = [("monday", 8), ("tuesday", 8), ("wednesday", 12), ("thursday", 4), ("friday", 5)]
overdue_work_hours6 = {day: hours for day, hours in work_hours if hours > 8}
print(overdue_work_hours6)
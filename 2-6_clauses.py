# Выбор холодильника
# TODO: нас интересуют только вендоры Brrr и SMF
# TODO: размер входной двери 210x90 мм
# TODO: размер панорманого окна 170X320 мм
# TODO: Холодильник наклонять нельзя, т.к. он с едой

if __name__ == '__main__':
    vendor = input()
    fridge_height = int(input())
    fridge_width = int(input())

    is_fitting_in_door = fridge_height <= 210 and fridge_width <=90
    is_fitting_in_window = fridge_height <= 170 and fridge_width <=320
    is_right_brand = vendor in ('Brrr', 'SMF')

    if is_right_brand and (is_fitting_in_door or is_fitting_in_window):
        print('Подходит')
    else:
        print('Не подходит')

#2-6-4
language = "Python"
position = "Ops"
print(f"Изучить {language} " , end="")
if "o" in language.lower() and not "g" in language:
    print("намного проще", end="")
else:
    print("проще", end=" ")
print(", чем сопромат")
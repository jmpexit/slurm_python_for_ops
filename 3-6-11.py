variable = "global"  # глобальная переменная
def main():
    variable = "enclosed"  # нелокальная переменная
    variable1 = "enclosed_from_inside_sub"  # локальная переменная
    variable2 = "enclosed2"
    def sub_main():
        variable = "local"  # локальная переменная
        print(variable)
        print(variable1)
        nonlocal variable2
        variable2 = "enclosed2_changed"
        print(variable2)
    sub_main()
    print(variable)
if __name__ == '__main__':
    main()
    print(variable)
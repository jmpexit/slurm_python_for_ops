
#TODO В последовательности frequency_data хранятся частоты встречаемости слов в тексте.
#TODO Постройте правильное выражение dictionary comprehension.


frequency_data = {"слово": 14, "и": 15432, "затем": 3422}

def format_key(dict):
    for k, v in dict:
        return str(k)


format_key(frequency_data)


def main():
    values = {format_key(k): v for k, v in frequency_data if v > 100}
    print(values)


if __name__ == '__main__':
    main()


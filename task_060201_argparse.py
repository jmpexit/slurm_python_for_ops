#!/bin/python3
import sys, os, argparse

# ip_addresses = sys.argv[1]  # sys.argv - список аргументов где 0 элемент - название файла со скриптом
# commands = sys.argv[2]
# input_line = "echo -e \"[\'123.123.123.123\', \'321.321.321.321\']\\n[\'ls -la\', \'ps uxwww\']\" | python3 your_programm.py"

def main():
    # конструктор класса ArgumentParser
    parser = argparse.ArgumentParser(description='Convert input string to ips and cmds',  # даем описание
                                     prog='task_621',  # указываем именование программы, кот.д/б запущена
                                     epilog='BYE'  # эпилог : то , чем будет завершена страница хэлпа
                                    # argument_default=0 # аргументы по умолчанию, только если аргумент - опциональный
                                    # prefix_chars='+'  # префикс вместо минуса, если вдруг захотелось
                                     )


    #создаем новые аргументы парсера и тем самым - новые члены класса
    # parser.add_argument('ip_addresses') # позиционный аргумент
    # parser.add_argument('-c', '--commands') # опциональный аргумент, с коротким именованием

    # parser.add_argument('-j', '--json_file',
    #                     metavar='path\\to\\your.json',  #  меняет плейсхолдеры,
    #                     help='путь до жысона',  # пояснения к хэлп странице
    #                     required=True)
    #
    # # можно задавать тип аргумента
    # parser.add_argument('-v',
    #                     help='is validation required',
    #                     type=bool)


    # parser.add_argument('ip_addresses',
    #                     type=list)  # так не работает
    #parser.add_argument('commands')

    # parser.add_argument('-v',
    #                     help='is validation required',
    #                     action='store_false')  # позволяет по (не)вводу ключа совершить к-л действие
                    # в этом случае: если ввести -v в команду, то значение аргумента станет False
                    # если не вводить - True
                    # action 'store_false' работает противоположно
                    # action='count' позволит посчитать количество введенных ключиков (-vvvvvv)
                    # action='append' сгенерит список из нескольких значений ключей (-v 1 -v 2)

    # parser.add_argument('-c', '--commands',
    #                     action='append'
    #                     )
                        # python .\task_060201_argparse.py -c 123.123.123.123 -c 123.123.123.5


    #parser.add_argument('-c', '--commands',
                        #nargs=3 # number of args
                        #nargs='?', # либо 0, либо 1
                        #default=0 # дефолт на уровне аргумента. удобно сочетать с nargs='?', т.к будет либо 0, либо то, что ввели
                        #nargs='*' # любое количество
                        #nargs='+' # 1 или более
     #                   )

    # переопределяем название
    # parser.add_argument('-c', '--commands',
    #                     dest='is command'
    #                    )
    #
    # args = parser.parse_args()
    #
    # print(type(args))
    # print(args)


    # ВЛОЖЕННОЕ МЕНЮ. САБПАРСЕРЫ
    subparsers = parser.add_subparsers(title='My subparsers',
                                       help='My subparsers help')

    subparser_1 = subparsers.add_parser(name='yaml', help='yaml help')
    subparser_2 = subparsers.add_parser(name='json', help='json help')

    subparser_1.add_argument('-y', '--yaml_file')
    subparser_2.add_argument('-j', '--json_file')

    args = parser.parse_args()

    print(args)

    #  python .\task_060201_argparse.py -h
    #  python .\task_060201_argparse.py json -h

if __name__ == '__main__':
    main()

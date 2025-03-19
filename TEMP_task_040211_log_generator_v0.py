#!/bin/python3

# !!! работает через python TMP_task_040211_log_generator_v0.py echo -e "['123.123.123.123', '221.221.221.221', '201.201.201.201']\n['ls -la', 'ps uxwww', 'rm -rf /']"

# поток ввода - Список IP в формате: ['XXX.XXX.XXX.XXX', 'XXX.XXX.XXX.XXX']
# поток ввода - список команд, которые нужно выполнить на хостах в формате: ['command', 'command']
# сформировать лог-сообщения, какие команды были выполнены на хосте: На хосте 123.123.123.123 была выполнена команда ls -la
# Если была встречена команда 'rm -rf /' - то нужно остановить выполнение всей программы
# и вывести сообщение: На хосте 321.321.321.321 была попытка выполнить команду rm -rf / , но процесс выполнения был аварийно остановлен.
# also try json.loads('[1,2,3]'), eval("[1, 2, 3]"), .splitlines())


import sys, os, json

ip_addresses_and_commands = sys.argv[3]  # sys.argv - список аргументов где 0 элемент - название файла со скриптом
ips, cmds = ip_addresses_and_commands.split('\\n')

ip_addresses = ips.translate({ord(i): None for i in '[]"\''}).split(', ')
commands = cmds.translate({ord(i): None for i in '[]"\''}).split(', ')

# ip_addresses = re.sub("[]", "", ips)
# commands = re.sub("[]", "", cmds)

# ip_addresses = ast.literal_eval(ips)
# commands = ast.literal_eval(cmds)

def generate_hosts(my_ip):
    for x in my_ip:
        yield x

def generate_commands(my_cmd):
    for x in my_cmd:
        yield x

def main():
    #print(list(zip(ip_addresses, commands)))
    for k, v in zip(generate_hosts(ip_addresses), generate_commands(commands)):
        if v != 'rm -rf /':
            print('На хосте', k, 'была выполнена команда', v)
        else:
            print('На хосте', k, 'была попытка выполнить команду', v, ', но процесс выполнения был аварийно остановлен.')
            break


if __name__ == '__main__':
    main()



#
# def main():
#     ip_addresses = generate_hosts()
#     commands = generate_commands()
#     values = dict(zip(ip_addresses, commands)
#                   for k, v in values.items():
#     if v != 'rm -rf /':
#         print('На хосте', k, 'была выполнена команда', v)
#     else:
#         print('На хосте', k, 'была попытка выполнить команду', v, ', но процесс выполнения был аварийно остановлен.')
#     break
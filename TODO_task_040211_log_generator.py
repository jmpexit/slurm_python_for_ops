#!/bin/python

# работает через echo

# поток ввода - Список IP в формате: ['XXX.XXX.XXX.XXX', 'XXX.XXX.XXX.XXX']
# поток ввода - список команд, которые нужно выполнить на хостах в формате: ['command', 'command']
# сформировать лог-сообщения, какие команды были выполнены на хосте: На хосте 123.123.123.123 была выполнена команда ls -la
# Если была встречена команда 'rm -rf /' - то нужно остановить выполнение всей программы
# и вывести сообщение: На хосте 321.321.321.321 была попытка выполнить команду rm -rf / , но процесс выполнения был аварийно остановлен.
# Значения будут подавать автоматически следующим способом: echo -e "['123.123.123.123', '321.321.321.321']\n['ls -la', 'ps uxwww']" | python3 your_programm.py

import sys, os, ast

ip_addresses_and_commands = input_data = sys.stdin.read()
ips, cmds = ip_addresses_and_commands.split('\\n')

ip_addresses = ast.literal_eval(ips)
commands = ast.literal_eval(cmds)

# ip_addresses = ips.translate({ord(i): None for i in '[]"\''}).split(', ')
# commands = cmds.translate({ord(i): None for i in '[]"\''}).split(', ')


def generate_hosts(my_ip):
    for x in my_ip:
        yield x

def generate_commands(my_cmd):
    for x in my_cmd:
        yield x

def main():
    for k, v in zip(generate_hosts(ip_addresses), generate_commands(commands)):
        if v != 'rm -rf /':
            print('На хосте', k, 'была выполнена команда', v)
        else:
            print('На хосте', k, 'была попытка выполнить команду', v, ', но процесс выполнения был аварийно остановлен.')
            break


if __name__ == '__main__':
    main()

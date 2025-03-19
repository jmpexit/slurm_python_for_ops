#!/bin/python

import sys, os, ast

ip_addresses_and_commands = sys.stdin.read()

ips, cmds = ip_addresses_and_commands.split('\\n')

ip_addresses = ips.translate({ord(i): None for i in '[]"\''}).split(', ')
commands = cmds.translate({ord(i): None for i in '[]"\''}).split(', ')

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

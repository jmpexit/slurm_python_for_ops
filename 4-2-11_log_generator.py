# поток ввода - Список IP в формате: ['XXX.XXX.XXX.XXX', 'XXX.XXX.XXX.XXX']
# поток ввода - список команд, которые нужно выполнить на хостах в формате: ['command', 'command']
# сформировать лог-сообщения, какие команды были выполнены на хосте: На хосте 123.123.123.123 была выполнена команда ls -la
# Если была встречена команда 'rm -rf /' - то нужно остановить выполнение всей программы
# и вывести сообщение: На хосте 321.321.321.321 была попытка выполнить команду rm -rf / , но процесс выполнения был аварийно остановлен.
#TODO Значения будут подавать автоматически следующим способом:
#TODO echo -e "['123.123.123.123', '321.321.321.321']\n['ls -la', 'ps uxwww']" | python3 your_programm.py - передача аргументов в питон снаружи, sys args


input_line = "echo -e \"[\'123.123.123.123\', \'321.321.321.321\']\\n[\'ls -la\', \'ps uxwww\']\" | python3 your_programm.py"

ip_addresses = ['123.123.123.123', '321.321.321.321', '222.222.222.222']
commands = ['ls -la', 'df -h', 'rm -rf /']


# def generate_hosts_with_commands(my_ip, my_cmd):
#     val = dict(zip(my_ip, my_cmd))
#     print(val)
#     yield val

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
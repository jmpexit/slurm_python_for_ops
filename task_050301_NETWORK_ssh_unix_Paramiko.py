import paramiko # pip3 install paramiko
#there is also netmika,

# build a container: 'docker-compose -f .\docker-compose.yaml up -d --build'
# check the connection: 'ssh -p 2222 service_user@localhost', and enter pwd (see docker-compose file)
# now you can use unix commands, such as 'ls'
# 'clear'


def main_simple():
     # establish connection
     with paramiko.SSHClient() as ssh_client: # instead of 'ssh_client = paramiko.SSHClient()' and 'ssh_client.close()'
         ssh_client.connect(hostname='localhost', port=2222,  # connect to the resource
                            username='service_user', password='q1w2e3')

def main_extended():
    with paramiko.SSHClient() as ssh_client:  # instead of 'ssh_client = paramiko.SSHClient()' and 'ssh_client.close()'
        ssh_client.load_system_host_keys() # If filename is empty, will read keys from the user's local "known hosts" file
        #ssh_client.load_system_host_keys(filename='/somepath')

        #ssh_client.set_missing_host_key_policy(paramiko.RejectPolicy) - another way to auth client (host)
        # RejectPolicy - rejects all connections from unknown / untrusted hosts
        # WarningPolicy - gives warning if a host is unknown, with establishing connection
        # AutoAddPolicy - automatically adds a host to authorized

        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh_client.connect(hostname='localhost', port=2222,  # connect to the resource
                               username='service_user', password='q1w2e3')


def main_print_commands():
    with paramiko.SSHClient() as ssh_client:
        ssh_client.load_system_host_keys()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh_client.connect(hostname='localhost', port=2222,
                            username='service_user', password='q1w2e3')

        # ssh_client.invoke_shell() # allocates pseudo-terminal. for apps with FE
        #.exec_command() # executes a command and returns 3 descriptors (stdin, stdout, stderr)

        stdin, stdout, stderr = ssh_client.exec_command('ls -la /')
        #print(stdout.read()) # will give a result in bytes
        print(stdout.read().decode('utf-8')) # decode bytes into string

def main_print_commands_stdout():
    with paramiko.SSHClient() as ssh_client:
        ssh_client.load_system_host_keys()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh_client.connect(hostname='localhost', port=2222,
                                   username='service_user', password='q1w2e3')

        # connect to ssh server container and allocate pseudo-terminal with 'docker exec -it openssh-server bash'
        # then go to /usr/bin and create file: 'vi echotest',
        # write in this file (after SHIFT, apparently):
        # #/bin/bash
        # echo 'Hi, choom!'
        # cat - # will read from input (stdin) and transfer it to output (stdout)
        # save with Esc :wq
        # make it executable 'chmod +x echotest'
        # this file is also now available from root directory
        # run it with 'echotest'
        # write anything in stdin - observe the same in stdout

        # NOTE: in contrast to the previous method, where after executing 'ls -la /'
        # the stdin/stdout flows were closed, here they do not

        # exit

        stdin, stdout, stderr = ssh_client.exec_command('echotest')  # run the code: nothing happens, as the script awaits stdin
        # it will be hanging forever

        #print(stdout.read(10)) # wait for 10 bytes
        #print(stdout.read(11)) # will hang again,because there are only 10 bytes (symbols) in the echotest file
        # and the program counts until the end, up to null terminator
        print('AAA')

        # we need to know how much data has our app (how many rows)
        print(stdout.readline())
        #print(stdout.readline()) # will hang again, because there are no new lines

        #stdin.write('Hi!') # will hang due to reading by rows
        stdin.write('Hi!\n')
        stdin.flush() # sometimes stdin is buffered file, and the buffer is not yet overloaded to sending,
                        # so we can use flush to force send
        print(stdout.readline())
        stdin.write('Hi!\n')
        stdin.flush()
        print(stdout.readline())


if __name__ == "__main__":
     main_print_commands_stdout()
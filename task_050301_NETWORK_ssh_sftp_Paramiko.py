import paramiko # pip3 install paramiko

#there is also netmika,

def main():
    key = paramiko.RSAKey.from_private_key_file('~/.ssh/id_rsa')
    with paramiko.SSHClient() as ssh_client:
        ssh_client.load_system_host_keys()
        #ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh_client.connect(hostname='localhost', port=22,
                           username='service_user', pkey=key)
        stdin, stdout, stderr = ssh_client.exec_command('ls -la /')
        # print(stdout.read().decode('utf-8'))

        stdin, stdout, stderr = ssh_client.exec_command('echotest')

        stdin.write('Hi!\n')
        stdin.flush()
        print(stdout.readline())
        stdin.write('Hi, world!\n')
        stdin.flush()
        print(stdout.readline())

        stdin, stdout, stderr = ssh_client.exec_command('task_generator erweErer')
        print(stderr.read())
        print(stdout.read())

        with ssh_client.open_sftp() as sftp_client:
            sftp_client.get(remotepath='/usr/bin/task_generator', localpath='./task_generator_2')
            try:
                sftp_client.put('txt.txt', remotepath='/txt.txt')
            except PermissionError:
                sftp_client.put('txt.txt', remotepath='/tmp/txt.txt')

            with sftp_client.open('txt.txt') as main_file:
                print(main_file.read().decode())

            try:
                sftp_client.rename(oldpath='/tmp/txt.txt', newpath='/tmp/txt_old.txt')
            except OSError:
                sftp_client.remove('/tmp/txt_old.txt')
                sftp_client.rename(oldpath='/tmp/txt.txt', newpath='/tmp/txt_old.txt')


            sftp_client.truncate(path='/tmp/txt_old.txt', size=0)

            print(sftp_client.getcwd())
            sftp_client.chdir('/tmp')
            print(sftp_client.getcwd())

            #sftp_client.chmod('txt_old.txt', 0755)
            sftp_client.chmod('txt_old.txt', 0o0755)
            sftp_client.chown('txt_old.txt', 0, 0)
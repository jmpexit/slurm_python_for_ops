import paramiko

# build a container: 'docker-compose -f .\docker-compose.yaml up -d --build'
# connect to it 'docker exec -it openssh-server bash'
# create a key with 'ssh-keygen -t rsa'
# copy pub key to the server
# you have to find , where authorized keys are on the server : root@:/config/.ssh# -> authorized_keys
# change it with vi: put your public key there


# DISCLAIMER: when we don't have server pwd, we can use keys
# def main_using_keys():
#     key = paramiko.RSAKey.from_private_key_file('C:\\keys\\rsa_key') # path on local machine with private key
#     with paramiko.SSHClient() as ssh_client:
#         ssh_client.load_system_host_keys()
#         #ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#         ssh_client.connect(hostname='localhost', port=2222,
#                             username='service_user', pkey=key,
#                            banner_timeout=400)
#     # authorize with 'ssh -p 2222 service_user@localhost' - the key must be used
#
#         print('Hi')

#def main_sftp():
        # ssh_client.invoke_shell()
        #.exec_command()

        # stdin, stdout, stderr = ssh_client.exec_command('task_generator erweErer')
        # print(stderr.read())
        # print(stdout.read())
        #
        # with ssh_client.open_sftp() as sftp_client:
        #     sftp_client.get(remotepath='/usr/bin/task_generator', localpath='./task_generator_2')
        #     try:
        #         sftp_client.put('txt.txt', remotepath='/txt.txt')
        #     except PermissionError:
        #         sftp_client.put('txt.txt', remotepath='/tmp/txt.txt')
        #
        #     with sftp_client.open('txt.txt') as main_file:
        #         print(main_file.read().decode())
        #
        #     try:
        #         sftp_client.rename(oldpath='/tmp/txt.txt', newpath='/tmp/txt_old.txt')
        #     except OSError:
        #         sftp_client.remove('/tmp/txt_old.txt')
        #         sftp_client.rename(oldpath='/tmp/txt.txt', newpath='/tmp/txt_old.txt')
        #
        #
        #     sftp_client.truncate(path='/tmp/txt_old.txt', size=0)
        #
        #     print(sftp_client.getcwd())
        #     sftp_client.chdir('/tmp')
        #     print(sftp_client.getcwd())
        #
        #     #sftp_client.chmod('txt_old.txt', 0755)
        #     sftp_client.chmod('txt_old.txt', 0o0755)
        #     sftp_client.chown('txt_old.txt', 0, 0)

if __name__ == "__main__":
    # main_using_keys()
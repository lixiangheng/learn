""" 登录SSH执行命令，返回结果！ """
import paramiko
from sys import argv


def sshlogoin(ip, port, user, passwd,execcmd):
    paramiko.util.log_to_file("paramiko.log")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, port=port, username=user, password=passwd)

    stdin, stout, stderr = ssh.exec_command(execcmd)
    stdin.write("Y")
    for line in stout:
        print(line.strip('\n'))
    ssh.close()


def main():
    ip = input('请输入需要连接的IP:')
    port = 22
    user = 'root'
    passwd = 'qwer1234'
    execmd = 'ls /root'
    sshlogoin(ip, port, user, passwd,execmd)


if __name__ == "__main__":
    main()



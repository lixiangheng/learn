""" 登录SSH执行命令，测试密码是否正确 """
import paramiko
import os


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
    with open('ip.txt', 'r') as f:
        for i in f.readlines():
            line = i.strip()
            port = 22
            user = 'root'
            passwd = 'Hn@1234567'
            execmd = 'ls /root'
            cmd = 'ping ' + line + ' -c 1'
            if os.system(cmd) == 0:
                try:
                    sshlogoin(line, port, user, passwd, execmd)
                    with open('log6', 'a') as A:
                        A.writelines('%s登录成功\n' % line)
                except paramiko.ssh_exception.AuthenticationException:
                    pass
                except TimeoutError:
                    pass
                except paramiko.ssh_exception.NoValidConnectionsError:
                    pass
            else:
                continue


if __name__ == "__main__":
    main()
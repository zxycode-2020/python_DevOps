import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    client.connect('192.168.6.13',22,'root','123')
    while True:
        cmd = raw_input('>>>')
        stdin,stdout,stderr = client.exec_command(cmd)
        print stdout.read(),
except Exception as e:
    print str(e)

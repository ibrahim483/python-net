from subprocess import Popen, PIPE
p = Popen(['ping', '-c 1', 'www.google.com'], stdout=PIPE)
while True:
    line = p.stdout.readline()
    if not line:
        break
    print(line)

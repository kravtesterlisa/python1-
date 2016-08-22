import subprocess
subprocess.call(['rsync','--update', '/root/test.txt', '/tmp/'], shell=True)

#subprocess.call()


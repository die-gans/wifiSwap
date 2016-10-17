import subprocess

def connect_to_network(name):                   #need to check if connected successfully TODO
    process = subprocess.Popen(
        'netsh wlan connect {0}'.format(name),
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print("connected to: " + name)

def create_profile():#TODO

    return
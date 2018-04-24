import os

def read(filename):
    return os.popen("cat %s " % filename).read().rstrip()

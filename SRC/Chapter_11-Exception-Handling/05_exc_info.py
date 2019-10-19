import sys

try:
    1 / 0
except:
    err = sys.exc_info()
    for e in err:
        print(e)

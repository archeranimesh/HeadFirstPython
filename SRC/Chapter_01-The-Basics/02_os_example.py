from os import getcwd
import datetime
import os
import sys
import time

print("getcwd(): ", getcwd())
print("sys.platform: ", sys.platform)
print("sys.version: ", sys.version)
print("os.envion: ", os.environ)
print("os.getenv('HOME'): ", os.getenv("HOME"))
print("datetime.date.today(): ", datetime.date.today())
print(
    "datetime.date.isoformat(datetime.date.today()): ",
    datetime.date.isoformat(datetime.date.today()),
)

print("%H:%M: ", time.strftime("%H:%M:%A %p"))

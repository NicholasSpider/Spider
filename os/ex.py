import sys
import os
import platform
import subprocess

print(sys.platform)
print(sys.platform.lower())
print(sys.platform.lower().startswith(''))
print(sys.platform.startswith(''))
print(os.name)
print(os.uname)
print(platform.platform())
print(platform.uname())
print(platform.system())
print(platform.machine())
print(platform.processor())
print(os.getgid())



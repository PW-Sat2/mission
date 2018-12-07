import os

for root, dirs, files in os.walk("sessions/"):
    print(root)
    print(dirs)
    print(files)
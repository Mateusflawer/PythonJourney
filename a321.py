import subprocess
import sys

print(sys.platform)


cmd = ["ping", "google.com"]

proc = subprocess.run(
    cmd, capture_output=True
)

print()
print(proc.stdout.decode("cp850"))

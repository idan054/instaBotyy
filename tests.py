import sys


def add(a, b):
  return a + b


"""
You need to execute the script add.py as follows:
'python add.py 5 2'
The 'sys.argv[0]' is the name of your script,
so you need to get the second and the third one.
"""

print(
    add(int(sys.argv[1]), int(sys.argv[2]))
)

"""
With the command: 'python add.py 5 2',
this python script will returns 7
"""

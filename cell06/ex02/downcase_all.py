import sys

def downcase_it(s):
    return s.lower()

args = sys.argv[1:]

if not args:
    print("Hello world")
else:
    for arg in args:
        print(downcase_it(arg))
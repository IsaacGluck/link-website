import os

files = os.listdir('/Users/isaacgluck/Desktop/github/')

for f in files:
	print(os.path.abspath(f))
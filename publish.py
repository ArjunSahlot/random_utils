import os
import re
import subprocess


def get_next_version(string):
	new = str(int(string.replace(".", "")) + 1)
	new = "0"*(3-len(new)) + new
	return new[0] + "." + new[1] + "." + new[2]


with open(os.path.join(os.path.realpath(os.path.dirname(__file__)), "setup.py"), "r") as orig:
	text = orig.read()
	pos_start = re.search(r"\d+\.\d+\.\d+", text).start()
	pos_end = re.search(r"\d+\.\d+\.\d+", text).end()
	text = text[:pos_start] + get_next_version(text[pos_start:pos_end]) + text[pos_end:]
	with open(os.path.join(os.path.realpath(os.path.dirname(__file__)), "setup.py"), "w") as f:
		f.write(text)

os.chdir(os.path.realpath(os.path.dirname(__file__)))

_ = subprocess.Popen(["twine", "upload", "dist/*"], stdin=subprocess.PIPE, stdout=subprocess.PIPE).communicate(input="USERNAME\nPASSWORD\n")

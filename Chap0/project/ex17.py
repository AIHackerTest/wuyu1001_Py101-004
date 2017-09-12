from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))


in_put = open(from_file)
in_data = in_put.read()

print("The input file is %d bytes long" % len(in_data))

print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

output = open(to_file, 'w')
output.write(in_data)

print("Alright, all done.")

output.close()
in_put.close()

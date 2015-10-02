import subprocess

output = subprocess.check_output(['ping', '-c', '3', 'adafruit.com'])

#all the following commented out lines are the long form way to parse the output
#output = output.splitlines()[1:-4]

#arr = []
#for line in output:
#	cleaned = line.rpartition("=")[-1]
#	cleaned = cleaned.partition(" ")[0]
#	arr.append(float(cleaned))

#all the above code can be condensed into one line as shown below
arr = [float(line.rpartition("=")[-1].partition(" ")[0]) for line in output.splitlines()[1:-4]]

#print the average using the standard python sum and len functions
print sum(arr) / len(arr)


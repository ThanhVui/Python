#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and
#compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ") # Prompt the user for a file name
# Open the file with the provided name
fh = open(fname)# Open the file for reading
n = 0 # for amount of lines
n1 = 0 #for summ
xDSPAM = 0# for xDSPAM confidence
nfloat = float(n)# Initialize nfloat to 0.0
for line in fh:# Loop through each line in the file
    if not line.startswith("X-DSPAM-Confidence:") : continue
    n = n + 1# Increment the line count
    xDSPAM = line[line.find('0') : ]# Extract the substring starting from the first '0'
    xDSPAMfl = float(xDSPAM)# Convert the extracted substring to a float
    n1 = n1 + xDSPAMfl# Add the float value to the sum
median = n1 / n# Calculate the average
print("Average spam confidence:", median)# Print the average spam confidence
# Read in the file
arcout_file_directory = "C:\\Users\luq\Desktop\\arcout.txt"
#============================================================================
filedata = None
with open(arcout_file_directory, 'r') as file:
  filedata = file.read()

# Replace the target string
filedata = filedata.replace("@@",",")

# Write the file out again
with open(arcout_file_directory, 'w') as file:
  file.write(filedata)

# Read in the file
#============================================================================
with open(arcout_file_directory, 'r') as file:
  filedata = file.readlines()
  for line in filedata:
      print(line)

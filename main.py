
# starting a for loop that will iterate through "line"(s)
# of .readlines() from the open .txt file that is opened
# directly in the for loop

for line in open("Project2.txt", "r").readlines():
    line = (line.strip().split(":"))
    print(f'{line[0]}: {line[2]}')

# open_file = open("Project2.txt", "r")
# open_file_lines = open_file.readlines()
# for line in open_file_lines:
#     line = line.strip().split(":")
#     print(f'{line[0]}: {line[2]}')






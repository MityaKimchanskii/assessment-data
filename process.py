log_file = open("um-server-01.txt") # this means we create new variable "log_file" which is text file with data, and for work we open this file


def sales_reports(log_file):  # It's a function called "sales_reports" that has 1 parameter "log_file"
    for line in log_file:     # we looping over this text file each line 
        line = line.rstrip()  # then we use method "rstrip()" for each line
        day = line[0:3]       # then we create new variable "day" equals to line[0:3] which means three first letters
        if day == "Mon":      # and then we checked if it's equals "Mon" or any day of week 
            print(line)       # if it's true then print line if not false and skip the line


# sales_reports(log_file)       # this line means we are call the function to see and check result

def melons(log_file):
    for line in log_file:
        line = line.rstrip()
        order = int(line[16:18])
        if order > 10:
            print(line)

melons(log_file)

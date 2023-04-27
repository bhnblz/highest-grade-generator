import pyfiglet
description = "Program 2: Name and GWA Generator"
print(pyfiglet.figlet_format(description.center(15)))

import colorama
from colorama import Fore

introduction = "Hi, here's the output of this program" 
print(Fore.LIGHTRED_EX + "=" * 92)
print(Fore.LIGHTRED_EX + (introduction.center(92)))
print("=" * 92)

# Open the file for reading
with open("students.txt") as main_file:
    # Initialize variable to keep track of the name who got the highest GWA and his/her GWA
    highest_gwa = 5.00
    student_highest = ""
    # Loop through each line in the file
    for line in main_file:
        # Split line into the student's GWA and name
        gwa = line.split(",")
        name = gwa[0]
        # Convert GWA to float
        gwa = float(gwa[1])
        # If highest
        if gwa < highest_gwa:
            highest_gwa = gwa
            student_highest = name

# Print the output
print(Fore.LIGHTMAGENTA_EX + "The student with the highest grade or GWA is " + (str(student_highest)), "with a GWA of " + (str(highest_gwa)),". Congratulations!")
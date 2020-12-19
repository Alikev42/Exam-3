#########1#########2#########3#########4#########5#########6#########7#########8
# Kevin R. Salger
# IS 640 Business Application Programming (Python)
# 
#########1#########2#########3#########4#########5#########6#########7#########8
#        11111111112222222222333333333344444444445555555555666666666677777777778
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#########1#########2#########3#########4#########5#########6#########7#########8
"""
Exam 3 (Final), Task 1
Question 1 (150 points for q1.py)

Write a program that performs the following tasks:

-	(10 points) Set the random seed to 2020 
-	(20 points) Randomly generate 10,000 numbers between 1000 and 2000 (inclusive) 
-	(50 points) Find all numbers that are 
o	even numbers and 
o	can be divided by 7 
-	(50 points) Count the frequency of the above numbers. Tips: you may want to use a dictionary.
-	(20 points) Display the numbers in ascending order and their frequencies as the following (sample output showing the format, not the real result):

1008 17
1022 19
1036 15
…
"""
#########1#########2#########3#########4#########5#########6#########7#########8
# Imported Modules
import random

#########1#########2#########3#########4#########5#########6#########7#########8
# Global Constants

#########1#########2#########3#########4#########5#########6#########7#########8
# Global Variables

#########1#########2#########3#########4#########5#########6#########7#########8
# Functions
#--------1---------2---------3---------4---------5---------6---------7---------8#

#--------1---------2---------3---------4---------5---------6---------7---------8#

#########1#########2#########3#########4#########5#########6#########7#########8
# Main
# Set random seed to 2020
random.seed(2020)
rand_dict = {}

# Randomly generate 10,000 numbers between 1000 and 2000 (inclusive)
for siffra in range(10000):
    temp_num = random.randrange(1000,2001)
    if temp_num in rand_dict.keys():
       rand_dict[temp_num] += 1
    else:
       rand_dict[temp_num] = 1

# Find all numbers that are even numbers and can be divided by 7
for cyfrif in rand_dict.keys():
    # Check for even, mod by 2
    if float(rand_dict[cyfrif]) % 2 != 0.0:
        rand_dict[cyfrif] = -1  # Set non-compliant entries to -1
    if float(rand_dict[cyfrif]) % 7 != 0.0:
        rand_dict[cyfrif] = -1  # Set non-compliant entries to -1

for num, cuenta in sorted(rand_dict.items()):
    if rand_dict.values() != -1:  # This is supposed to weed out entries with value = -1
        print(f'{num} {cuenta}')

#print(rand_dict)
# End of Main 
#########1#########2#########3#########4#########5#########6#########7#########8
# Kevin R. Salger
# IS 640 Business Application Programming (Python)
# 
#########1#########2#########3#########4#########5#########6#########7#########8
#        11111111112222222222333333333344444444445555555555666666666677777777778
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#########1#########2#########3#########4#########5#########6#########7#########8
"""
Exam 3 (Final), Task 2
Question 2 (150 points for q2.py)

The “alice.txt” is a text file that has multiple lines. It has the following content:

Alice was beginning to get very tired of sitting by her sister on the bank
and of having nothing to do
once or twice she had peeped into the book her sister was reading
but it had no pictures or conversations in it
and what is the use of a book
thought Alice
without pictures or conversations…

Write a program q2.py that performs the following tasks:
1)	(50 points) Read the file and create a dictionary that each word in the text file is a key, the value is the line numbers that the word appears in the file. The first line number is 1. If a word appears in a line multiple times, only put the line number once. For example, “it” appears in line 4 two times, only put one “4” as its value.
2)	(50 points) Calculate the frequency of each word appears in the file. For example, “Alice” has a frequency of 2, in line 1 and line6. “it” has a frequency of 2, both in line 4. 
3)	(50 points) Write an output file named “index.txt”. The output is sorted by the key in ascending order: key, frequency and list of line numbers separated by a space. The format is “Key (frequency): line1 line2 line3”. The following is a partial content of the generated “index.txt”: 

Alice (2): 1 6 
beginning (1): 1
book (2): 3 5
…
it (2): 4
…
without (1): 7


"""
#########1#########2#########3#########4#########5#########6#########7#########8
# Imported Modules


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
text = {}
count_words = {}
line_count = 0
line_list = []

#  Read the book.txt file
try:
    with open('alice.txt',mode='r') as BookText: # Open the text file book.txt
        for book_line in BookText: # Reading line by line of text
            line_count += 1             
            for each_word in book_line.split(): # Read each word
                if each_word in text:
                    count_words[each_word] += 1
                else:
                    count_words[each_word] = 1
                # Now have dictionary with frequency of words
                if each_word in text.keys():
                    text[each_word] = [line_list.append(line_count)]
except:
    print('The file \'alice.txt\' does not exist.')
    quit()  # Python threw an exception at this line.  Find solution.....

# Output
with open ('index.txt', mode='a+') as output: 
    for word in each_word.items():
        print(f'{each_word.keys[word]} ({each_word.values}): {text.values()}', file = output)
# End of Main 
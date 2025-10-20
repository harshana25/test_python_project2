# Define numer dictionary with word

num_list={
    "0":"zero",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine"


}


# get the user input for the numbers
numbers = input('Enter the numbers separated by a comma: ')

# create a list for user's input based on their input behaviour
if "," in numbers:
    numbers = numbers.split(',')
else:
    numbers = list(numbers)

# Define an empty list for adding the output
words = []

# Looping through the numbers and find the relevant word from the list
# matching with user's input
for number in numbers:
    find_word = num_list.get(number.strip(),"Invalid input")
    words.append(find_word)

for word in words:
    print(word)


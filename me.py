# Ask user for text and make all letters lowercase
text = input("Insert a text: ").lower()

# Ask user for 3 letters and make all letters lowercase
lettera = input("Input a random letter: ").lower()
letterb = input("Input another random letter: ").lower()
letterc = input("Input a third random letter: ").lower()

# Store user's letters in a list
letterlist = [lettera, letterb, letterc]
print(letterlist)

# Count how many times the user's 3 letters appear in the textabc
for letter in letterlist:
    print(text.count(letter))

# Convert user's text into a list
user_textlist = list(text)
print(user_textlist)

# Find the length of the list containing the user's text
print(len(user_textlist))

# Find the first letter in the list containing the user's text
print(user_textlist[0])

# Find the last letter in the list containing the user's text
print(user_textlist[-1])

# Invert the order of the elements in the list containing the user's text
reversed_text = user_textlist[::-1]
print(reversed_text)

# Join these elements in the list containing the user's text with spaces in between
joined_reversed_usertext = " ".join(reversed_text)
print(joined_reversed_usertext)

# Check if the word "python" is in the text with a boolean and display the result to the user
print("python" in user_textlist)
##############
##############
############################################################################################################################Extra Challenge############################
sentence = "In practice, good communication is key in collaborative programming."
#Step 1
#A  Display the index of the first occurrence of the word "good"
first_good_index = sentence.index("good") 
print("First occurrence of 'good':", first_good_index)

#B Display the index of the last occurrence of the word "in"
last_in_index = sentence.rindex("in")
print("Last occurrence of 'in':", last_in_index) 

#Step 2: Create a list from the sentence, reverse the order of the words, and join them back into a string words
sentence.split() reversed_sentence = ' '.join(reversed(words)) 
print("Reversed sentence:", reversed_sentence)


 


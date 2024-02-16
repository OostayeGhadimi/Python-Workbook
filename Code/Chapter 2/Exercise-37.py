#Exercise 37:Vowel or Consonant

# Determine if a letter is a vowel or a consonant.

# Read a letter from the user
letter = input("Enter Your letter:")

# Classify the letter and report the result
if letter == ("a" or "e" or "i" or "o" or "u") :
    print("letter is a vowel.")
elif letter == "y" :
    print("sometimes y is a vowel, and sometimes y is a consonant.")
else :
    print(" the letter is a consonant.")
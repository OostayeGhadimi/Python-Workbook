# Read a number from the user
num = float(input("Enter a number: "))

# Store the appropriate message in result
if num > 0:
    # Determine what adjective should be used to describe the number
    adjective = " "
    if num >= 1000000:
        adjective = " really big "
    elif num >= 1000:
        adjective = " big "
    # Store the message for positive numbers including the appropriate adjective
    result = "That’s a" + adjective + "positive number"

elif num < 0:
    result = "That’s a negative number"
else:
    result = "That’s zero"

# Display the message
print(result)
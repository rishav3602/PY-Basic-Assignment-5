"""
7. What is a shortcut for the following code?
if 'color' not in spam:
spam['color'] = 'black'

"""

"""
Answer...

spam['color'] = 'black' if 'color' != spam else print("It is present")

    """



spam = {"boy":"ladka"}
spam['color'] = 'black' if 'color' != spam else print("It is present")
print(spam) #it will also show color now



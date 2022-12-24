"""
6. If a dictionary is stored in spam, what is the difference between the 
expressions 'cat' in spam and 'cat' in spam.values()?
"""

"""
Answer...


"""
spam = {"cat":"billi"}
if 'cat'not in spam:
    print("Yes")
elif 'cat' in spam.values():
    print("No")
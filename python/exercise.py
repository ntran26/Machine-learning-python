# Ex 1: Given this nested dictionary grab the word "hello"
print('\nExercise 1')
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

# Ex 2: Create a function that grabs the email website domain from a string in the form: 'user@domain.com'
print('\nExercise 2')
def domainGet(email):
    return email.split('@')[1]      # split string by @ character and take the second index
email = 'glitterfart@xxx.com'
print('Domain of the email is: {}'.format(domainGet(email)))

# Ex 3: Create a basic function that returns True if the word 'dog' is contained in the input string
print('\nExercise 3')
def findDog(str):
    return 'dog' in str.lower().split()     # transform to lower case, then split each word by white space

str = 'Is there a DoG here?'
print(findDog(str))

# Ex 4: Create a function that counts the number of times the word "dog" occurs in a string
print('\nExercise 4')
def countDog(str):
    count = 0
    for items in str.lower().split():
        if items == 'dog':
            count += 1
    return count
print('Number of dog words: {}'.format(countDog('This doG runs faster than the other Dog dude!')))

# Ex 5: You are driving a little too fast, and a police officer stops you. 
# Write a function to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
# If your speed is 60 or less, the result is "No Ticket". 
# If speed is between 61 and 80 inclusive, the result is "Small Ticket". 
# If speed is 81 or more, the result is "Big Ticket". 
print('\nExercise 5')
def caughtSpeed(speed):
    if speed <= 60:
        print('No ticket')
    elif speed <= 80 and speed >= 61:
        print('Small ticket')
    elif speed > 80:
        print('Big ticket')

caughtSpeed(80)

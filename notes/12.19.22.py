# String Interpolation - allows the computer to parse the string
name = 'Leo'
age = 41

print(name + ' is ' + str(age) + ' years old!')
print(name, 'is', str(age), 'years old!')

print(f"{name} is {age} years old!")

class User:
    first_name = None
    last_name = None

    def __init__(this, first, last):
        this.first_name = first
        this.last_name = last

    def get_name(this):
        return f"{this.first_name} {this.last_name}"

    def __get_length(thism, data):
        return len(data)

user = User("John", "Doe")
# String interplation while calling a function
print(f"{user.get_name()} was the first user in the system!")

# snake case variables/functions
first_name = ''
def get_first_name():
    print(first_name)

# Upper Camel classes -> Try not to use "lowerCamel" anymore
class PingPong:
    ball = 0

# Constants (data that should never change or be changed) - ALL UPPER CASE
VELOCITY = 3.14
NUMBER_PLAYERS = 2

# Classes that only a function uses should be prefixed with '__' like "__class_name"
# See User class above


'''
Reading in a file, storing the value, adding/modifying any entries, re-writing file
Example data
Joe,5
Mark,7
John,2
'''

scores = {}
f = open("scores.csv", 'r') # open file
# read the entire contents, writing every new line to our scores list
scores['column1'] = 'column2'
# if user in scores
    #scores[user] += new_score
# once the round is over, scores should hold all current users with scores as
# well as the new users at the bottom of the list
# Just write all of this to your file again

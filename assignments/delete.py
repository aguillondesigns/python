# delete.data - file used for testing
'''
john
mark
paul
steven
brad
'''

# Method 1 - delete based on search criteria
# just gathering the file data here
f = open('delete.data', 'r')
lines = f.readlines()
f.close()

criteria = "mark"
f = open('delete.data', 'w')
for line in lines:
    if criteria not in line:
        f.write(line)
f.close()


# Method 2 - dynamic id delete
class User:
    user_id = None
    username = None

    def __init__(this, id, username):
        this.user_id = id
        this.username = username
        
    def __str__(this) -> str:
        return f"{this.user_id} - {this.username}"

users = []

def load_users():
    global users
    users = []
    f = open('delete.data', 'r')
    lines = f.readlines()
    f.seek(0,0)
    current_line = 0
    while current_line <= len(lines):
        line = f.readline().strip()
        if (line != ''):
            users.append(User(str(current_line + 1), line))
        current_line += 1

def delete_user(id):
    f = open('delete.data', 'w')
    for user in users:
        if user.user_id != id:
            f.write(user.username + "\n")
    f.close()
    load_users()

def show_users():
    print("Current Users:")
    for user in users:
        print(user)

load_users()
show_users()
choice = input("User id to remove: ")
delete_user(choice)
print(f"attempting to delete ({choice})")
show_users()


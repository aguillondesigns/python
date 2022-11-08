# Lets us know if the file exists or not
def fileExists(filename):
    try:
        f = open(filename, "x")
        f.close()
        return True
    except:
        return False

print("Enter filename:")
filename = input()
if fileExists(filename) == False:
    print("file exits already, appending...")
    f = open(filename, 'a')
else:
    print("creating new file")
    f = open(filename, 'w')

f.write("some data" + "\n")
f.write("some more data" + "\n")
f.close()


f2 = open(filename, "r")
print(f2.read())